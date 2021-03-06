# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-07 18:46
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def update_program_activity_records(apps, schema_editor):
    """Run new program activity loader."""
    call_command('loadprogramactivity', 'usaspending_api/data/program_activity.csv')


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0061_auto_20170404_2153'),
    ]

    operations = [
        migrations.RunPython(update_program_activity_records, migrations.RunPython.noop),
    ]
