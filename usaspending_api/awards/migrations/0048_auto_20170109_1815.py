# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-09 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0047_auto_20161222_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurement',
            name='number_of_actions',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
