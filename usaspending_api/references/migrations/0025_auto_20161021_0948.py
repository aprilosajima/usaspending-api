# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0024_refcfdaprograminfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refcfdaprograminfo',
            name='program_number',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
    ]
