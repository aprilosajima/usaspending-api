# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0023_auto_20161013_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefCFDAProgramInfo',
            fields=[
                ('program_number', models.TextField(primary_key=True, serialize=False)),
                ('program_title', models.TextField(blank=True, null=True)),
                ('popular_name', models.TextField(blank=True, null=True)),
                ('federal_agency', models.TextField(blank=True, null=True)),
                ('authorization', models.TextField(blank=True, null=True)),
                ('objectives', models.TextField(blank=True, null=True)),
                ('types_of_assistance', models.TextField(blank=True, null=True)),
                ('uses_and_use_restrictions', models.TextField(blank=True, null=True)),
                ('applicant_eligibility', models.TextField(blank=True, null=True)),
                ('beneficiary_eligibility', models.TextField(blank=True, null=True)),
                ('credentials_documentation', models.TextField(blank=True, null=True)),
                ('pre_application_coordination', models.TextField(blank=True, null=True)),
                ('application_procedures', models.TextField(blank=True, null=True)),
                ('award_procedure', models.TextField(blank=True, null=True)),
                ('deadlines', models.TextField(blank=True, null=True)),
                ('range_of_approval_disapproval_time', models.TextField(blank=True, null=True)),
                ('website_address', models.URLField(blank=True, null=True)),
                ('formula_and_matching_requirements', models.TextField(blank=True, null=True)),
                ('length_and_time_phasing_of_assistance', models.TextField(blank=True, null=True)),
                ('reports', models.TextField(blank=True, null=True)),
                ('audits', models.TextField(blank=True, null=True)),
                ('records', models.TextField(blank=True, null=True)),
                ('account_identification', models.TextField(blank=True, null=True)),
                ('obligations', models.TextField(blank=True, null=True)),
                ('range_and_average_of_financial_assistance', models.TextField(blank=True, null=True)),
                ('program_accomplishments', models.TextField(blank=True, null=True)),
                ('regulations_guidelines_and_literature', models.TextField(blank=True, null=True)),
                ('regional_or_local_office', models.TextField(blank=True, null=True)),
                ('headquarters_office', models.TextField(blank=True, null=True)),
                ('related_programs', models.TextField(blank=True, null=True)),
                ('examples_of_funded_projects', models.TextField(blank=True, null=True)),
                ('criteria_for_selecting_proposals', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('recovery', models.TextField(blank=True, null=True)),
                ('omb_agency_code', models.TextField(blank=True, null=True)),
                ('omb_bureau_code', models.TextField(blank=True, null=True)),
                ('published_date', models.TextField(blank=True, null=True)),
                ('archived_date', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'ref_cfda_program_info',
            },
        ),
    ]
