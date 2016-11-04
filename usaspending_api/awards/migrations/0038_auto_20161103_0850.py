# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0037_subaward'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='data_source',
            field=models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='financialaccountsbyawards',
            name='data_source',
            field=models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='financialaccountsbyawardstransactionobligations',
            name='data_source',
            field=models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='data_source',
            field=models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='procurement',
            name='data_source',
            field=models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='subaward',
            name='data_source',
            field=models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], max_length=3, null=True),
        ),
    ]