# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20170814_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_title',
            field=models.CharField(max_length=200),
        ),
    ]