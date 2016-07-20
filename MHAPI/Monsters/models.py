"""MHGen Monsters model."""

from __future__ import unicode_literals

from django.db import models

from Locations.models import Location


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


class Damage(models.Model):
    """Monster Damage Model."""

    monster = models.ForeignKey(Monster, related_name='damage')
    key = models.CharField(max_length=255, null=True, blank=True)
    body_part = models.CharField(max_length=255, null=True, blank=True)
    cut = models.CharField(max_length=255, null=True, blank=True)
    impact = models.CharField(max_length=255, null=True, blank=True)
    shot = models.CharField(max_length=255, null=True, blank=True)
    fire = models.CharField(max_length=255, null=True, blank=True)
    water = models.CharField(max_length=255, null=True, blank=True)
    ice = models.CharField(max_length=255, null=True, blank=True)
    thunder = models.CharField(max_length=255, null=True, blank=True)
    dragon = models.CharField(max_length=255, null=True, blank=True)
    ko = models.CharField(max_length=255, null=True, blank=True)


class Habitat(models.Model):
    """Monster Habitat Model."""

    monster = models.ForeignKey(Monster, related_name='habitat')
    location = models.ForeignKey(Location, related_name='monster')
    start_area = models.CharField(max_length=255, null=True, blank=True)
    move_area = models.CharField(max_length=255, null=True, blank=True)
    rest_area = models.CharField(max_length=255, null=True, blank=True)





