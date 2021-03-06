# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0008_armor_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('rarity', models.CharField(blank=True, max_length=255, null=True)),
                ('carry_capacity', models.CharField(blank=True, max_length=255, null=True)),
                ('buy', models.CharField(blank=True, max_length=255, null=True)),
                ('sell', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
