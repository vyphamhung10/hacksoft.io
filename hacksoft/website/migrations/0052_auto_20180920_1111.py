# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_auto_20180920_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostsnippet',
            name='search_description',
            field=models.TextField(blank=True, verbose_name='search description'),
        ),
        migrations.AddField(
            model_name='blogpostsnippet',
            name='seo_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='page title'),
        ),
    ]