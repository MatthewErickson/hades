# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 01:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hades', '0003_auto_20160912_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 12, 1, 37, 36, 217843, tzinfo=utc), verbose_name='date published'),
        ),
    ]
