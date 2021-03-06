# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-05 19:09
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import F


def forwards_or_backwards_func(apps, schema_editor):
    """
    Because -1 * -1 == 1, this migration works the same both directions!
    """
    db_alias = schema_editor.connection.alias

    AppropriationAccountBalances = apps.get_model(
        'accounts', 'AppropriationAccountBalances')
    AppropriationAccountBalances.objects.using(db_alias).update(
        gross_outlay_amount_by_tas_cpe=F('gross_outlay_amount_by_tas_cpe') * -1)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts',
         '0020_remove_appropriationaccountbalances_tas_rendering_label'),
    ]

    operations = [
        migrations.RunPython(forwards_or_backwards_func,
                             forwards_or_backwards_func),
    ]
