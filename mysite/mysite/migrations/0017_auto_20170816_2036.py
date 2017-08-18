# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20170816_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Cate', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]