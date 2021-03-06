# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_auto_20160718_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.CharField(blank=True, max_length=15, null=True)),
                ('key', models.CharField(blank=True, max_length=15, null=True)),
                ('wtype', models.CharField(blank=True, max_length=15, null=True)),
                ('creation_cost', models.CharField(blank=True, max_length=15, null=True)),
                ('uprgrade_cost', models.CharField(blank=True, max_length=15, null=True)),
                ('attack', models.CharField(blank=True, max_length=15, null=True)),
                ('element', models.CharField(blank=True, max_length=15, null=True)),
                ('element_attack', models.CharField(blank=True, max_length=15, null=True)),
                ('element_2', models.CharField(blank=True, max_length=15, null=True)),
                ('element_2_attack', models.CharField(blank=True, max_length=15, null=True)),
                ('defense', models.CharField(blank=True, max_length=15, null=True)),
                ('affinity', models.CharField(blank=True, max_length=15, null=True)),
                ('horn_notes', models.CharField(blank=True, max_length=15, null=True)),
                ('shell_type', models.CharField(blank=True, max_length=15, null=True)),
                ('phial', models.CharField(blank=True, max_length=15, null=True)),
                ('charges', models.CharField(blank=True, max_length=15, null=True)),
                ('coating', models.CharField(blank=True, max_length=15, null=True)),
                ('recoil', models.CharField(blank=True, max_length=15, null=True)),
                ('reload_speed', models.CharField(blank=True, max_length=15, null=True)),
                ('rapid_fire', models.CharField(blank=True, max_length=15, null=True)),
                ('deviation', models.CharField(blank=True, max_length=15, null=True)),
                ('ammo', models.CharField(blank=True, max_length=15, null=True)),
                ('special_ammo', models.CharField(blank=True, max_length=15, null=True)),
                ('num_slots', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
