# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-04-29 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_officials', '0003_auto_20170417_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislator',
            name='twitter_id',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
