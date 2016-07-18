"""Model for MHGen Items."""

from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    """Item Model Class."""

    name = models.CharField(max_length=255)
    key = models.CharField(max_length=15, null=True, blank=True)
    item_type = models.CharField(max_length=255, null=True, blank=True)
    item_subtype = models.CharField(max_length=255, null=True, blank=True)
    rarity = models.CharField(max_length=255, null=True, blank=True)
    carry_capacity = models.CharField(max_length=255, null=True, blank=True)
    buy = models.CharField(max_length=255, null=True, blank=True)
    sell = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)


class Weapon(models.Model):
    """Weapon Model Class."""

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    key = models.CharField(max_length=255, null=True, blank=True)
    wtype = models.CharField(max_length=255, null=True, blank=True)
    creation_cost = models.CharField(max_length=255, null=True, blank=True)
    upgrade_cost = models.CharField(max_length=255, null=True, blank=True)
    attack = models.CharField(max_length=255, null=True, blank=True)
    element = models.CharField(max_length=255, null=True, blank=True)
    element_attack = models.CharField(max_length=255, null=True, blank=True)
    element_2 = models.CharField(max_length=255, null=True, blank=True)
    element_2_attack = models.CharField(max_length=255, null=True, blank=True)
    defense = models.CharField(max_length=255, null=True, blank=True)
    affinity = models.CharField(max_length=255, null=True, blank=True)
    horn_notes = models.CharField(max_length=255, null=True, blank=True)
    shell_type = models.CharField(max_length=255, null=True, blank=True)
    phial = models.CharField(max_length=255, null=True, blank=True)
    charges = models.CharField(max_length=255, null=True, blank=True)
    coating = models.CharField(max_length=255, null=True, blank=True)
    recoil = models.CharField(max_length=255, null=True, blank=True)
    reload_speed = models.CharField(max_length=255, null=True, blank=True)
    rapid_fire = models.CharField(max_length=255, null=True, blank=True)
    deviation = models.CharField(max_length=255, null=True, blank=True)
    ammo = models.CharField(max_length=255, null=True, blank=True)
    special_ammo = models.CharField(max_length=255, null=True, blank=True)
    num_slots = models.CharField(max_length=255, null=True, blank=True)
