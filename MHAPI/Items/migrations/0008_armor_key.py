# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0007_auto_20160719_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='armor',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]