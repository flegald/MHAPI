# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monsters', '0003_habitat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buff',
            old_name='buff_type',
            new_name='status_type',
        ),
        migrations.AlterField(
            model_name='buff',
            name='monster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='Monsters.Monster'),
        ),
    ]
