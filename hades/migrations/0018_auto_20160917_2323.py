# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 06:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hades', '0017_auto_20160917_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 18, 6, 23, 15, 491321, tzinfo=utc), verbose_name='date published'),
        ),
    ]