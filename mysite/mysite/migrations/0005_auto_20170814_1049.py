# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 02:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20170814_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]