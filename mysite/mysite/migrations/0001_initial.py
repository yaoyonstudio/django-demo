# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 02:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_content', models.TextField()),
                ('page_title', models.TextField()),
                ('page_excerpt', models.TextField()),
                ('page_status', models.CharField(max_length=20)),
                ('page_name', models.CharField(max_length=200)),
                ('page_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
