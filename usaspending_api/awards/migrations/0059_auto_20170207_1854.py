# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-07 18:54
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import connection, migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0058_auto_20170208_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialaccountsbyawards',
            name='appropriation_account_balances',
        ),
    ]
