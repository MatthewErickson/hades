# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 05:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hades', '0008_auto_20160914_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='file_path',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 5, 22, 31, 44373, tzinfo=utc), verbose_name='date published'),
        ),
    ]
