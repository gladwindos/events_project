# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20160623_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='auth0_favourite_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, null=True, size=None),
        ),
    ]
