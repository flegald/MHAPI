"""MHGen Monsters model."""

from __future__ import unicode_literals

from django.db import models


class Monster(models.Model):
    """Monster Model."""

    key = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    mclass = models.CharField(max_length=255, null=True, blank=True)
    base_hp = models.CharField(max_length=255, null=True, blank=True)


class Buff(models.Model):
    """Buff Damage Model."""

    monster = models.ForeignKey(Monster, related_name='weaknesses')
    key = models.CharField(max_length=255, null=True, blank=True)
    buff_type = models.CharField(max_length=255, null=True, blank=True)
    initial = models.CharField(max_length=255, null=True, blank=True)
    increase = models.CharField(max_length=255, null=True, blank=True)
    dmax = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    damage = models.CharField(max_length=255, null=True, blank=True)







