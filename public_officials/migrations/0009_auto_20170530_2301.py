# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-30 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_officials', '0008_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='legislators',
            field=models.ManyToManyField(blank=True, to='public_officials.Legislator'),
        ),
    ]