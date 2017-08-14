# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 07:06
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0006_auto_20170814_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_title', models.CharField(max_length=100)),
                ('cate_desc', models.CharField(max_length=100)),
                ('cate_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cate_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_name', models.CharField(max_length=200)),
                ('post_status', models.BooleanField(default=True, verbose_name='page_status')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_excerpt', models.TextField()),
                ('post_content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Cate')),
            ],
        ),
    ]