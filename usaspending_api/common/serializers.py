from rest_framework import serializers
from usaspending_api.common.helpers import get_params_from_req_or_request


class LimitableSerializer(serializers.ModelSerializer):
    prefetchable = True

    """Extends the model serializer to support field limiting."""
    def __init__(self, *args, **kwargs):
        # next two lines are deprecated and will be removed
        # once all views inherit from a generic class or are
        # refactored into viewsets (i.e., once the serializer
        # consistently has direct access to the request)
        include_fields = kwargs.pop('fields', None)
        exclude_fields = kwargs.pop('exclude', None)
        super(LimitableSerializer, self).__init__(*args, **kwargs)

        # Create and initialize the child serializers
        try:
            # Initialize the child serializers
            children = self.Meta.nested_serializers
            for field in children.keys():
                child_args = {
                    **children[field].get("kwargs", {}),
                    "context": {**self.context, "child": True}
                }  # The child tag should be removed when child field limiting is implemented
                self.fields[field] = children[field]["class"](**child_args)
        except AttributeError:
            # We don't have any nested serializers
            pass

        req = self.context.get('req')
        request = self.context.get('request')

        if request:
            params = get_params_from_req_or_request(request=request, req=req)

            exclude_fields = params.get('exclude')
            include_fields = params.get('fields')
            current_viewset = self.context.get('view')

            if params.get('verbose', False):
                # We have a request for verbose, so we return here so that we
                # return all fields
                return

            # We must exclude before include to avoid conflicts from user error
            if exclude_fields is not None and not self.context.get("child", False):  # the child check should be removed when child field limiting is implemented
                for field_name in exclude_fields:
                    try:
                        self.fields.pop(field_name)
                    except KeyError:
                        # Because we're not currently handling nested serializer field
                        # limiting pass-down, this can happen due to the context pass down
                        pass

            if include_fields is not None and not self.context.get("child", False):  # the child check should be removed when child field limiting is implemented
                allowed = set(include_fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    try:
                        # If we have a coded field, always include its description
                        if field_name.split("_")[-1] == "description" and "_".join(field_name.split("_")[:-1]) not in allowed:
                            continue
                        self.fields.pop(field_name)
                    except KeyError:
                        # Because we're not currently handling nested serializer field
                        # limiting pass-down, this can happen due to the context pass down
                        pass

            elif current_viewset and current_viewset.action == 'retrieve':
                # The view has specifically asked that all fields should
                # be returned (for example, when the request url follows
                # the item/{pk} pattern)
                return

            else:
                try:
                    include_fields = self.Meta.model.get_default_fields(path=request._request.path_info)
                    allowed = set(include_fields)
                    existing = set(self.fields.keys())
                    for field_name in existing - allowed:
                        self.fields.pop(field_name)
                except AttributeError:
                    # We don't have get default fields available
                    pass

    @classmethod
    def setup_eager_loading(cls, queryset, prefix=""):
        '''
        This method will set up prefetch and selected related statements appropriately
        on a specified query set based upon the serializer's nested_serializer parameter
        in the Meta class. It will return the modified queryset.
        The prefix flag is for cascading down to children, that is, when we eager load
        a child of this serializer, we must prefix that child's field name to their field name.
        For example:
        AwardSerializer has a nested serializer of funding_agency with a nested serializer for toptier agency
        Thus, when we prefetch, we want to prefetch 'funding_agency' and 'funding_agency__toptier_agency'
        This prefix flag allows us to accomplish this.
        N.B.: When doing a 1-1 fk relation, select_related() should be used (this join is performed in the SQL);
              When doing a 1-m or m-m relation, prefetch_related() should be used (this join is performed via Python)
        '''
        try:
            # Grab the nested serializers (aka children)
            children = cls.Meta.nested_serializers
            for child in children:
                serializer_class = children[child]["class"]
                if (not hasattr(serializer_class, 'prefetchable')) or (not serializer_class.prefetchable):
                    continue
                queryset = queryset.prefetch_related(prefix + child)
                # Since the child might have nested serializers, we set up on that too
                queryset = serializer_class.setup_eager_loading(queryset, prefix=prefix + child + "__")
        except AttributeError:
            # We don't have any nested serializers
            pass

        return queryset


class AggregateSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super(AggregateSerializer, self).__init__(*args, **kwargs)

        include_fields = None

        req = self.context.get('req')
        if req:
            params = get_params_from_req_or_request(req=req)
            include_fields = params.get('group')
            if not isinstance(include_fields, list):
                include_fields = [include_fields]

        if include_fields:
            for field_name in include_fields:
                if field_name is None:
                    continue
                self.fields[field_name] = serializers.CharField(required=False)

    item = serializers.CharField(required=False)
    aggregate = serializers.DecimalField(20, 2)
