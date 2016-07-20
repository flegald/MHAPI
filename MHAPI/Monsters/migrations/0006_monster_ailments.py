# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 19:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monsters', '0005_weakness'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='ailments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
    ]
