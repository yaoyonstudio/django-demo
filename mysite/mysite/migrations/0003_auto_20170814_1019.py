# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20170814_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_status',
            field=models.BooleanField(default=True, verbose_name='page_status'),
        ),
    ]