# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-30 14:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 7, 30, 14, 10, 35, 574391, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
