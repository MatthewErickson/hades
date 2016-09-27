# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 01:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hades', '0002_auto_20160911_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2016, 9, 12, 1, 36, 57, 431618, tzinfo=utc), verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
