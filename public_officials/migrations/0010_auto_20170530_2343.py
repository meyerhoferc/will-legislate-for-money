# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-05-30 23:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public_officials', '0009_auto_20170530_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersLegislators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legislator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='public_officials.Legislator')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='legislators',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userslegislators',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
