# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Locations', '0002_location_map_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='key',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
