# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_blogpostspage_featured_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='how_we_work_center',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='how_we_work_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='how_we_work_title',
        ),
    ]