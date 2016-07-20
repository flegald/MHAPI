"""MH Generations Quest Models."""

from __future__ import unicode_literals

from django.db import models
from Locations.models import Location


class Quest(models.Model):
    """Quest Model."""

    key = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    qtype = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Location, related_name='quests')
    goal = models.CharField(max_length=255, null=True, blank=True)
    hub = models.CharField(max_length=255, null=True, blank=True)
    rank = models.CharField(max_length=255, null=True, blank=True)
    goal_type = models.CharField(max_length=255, null=True, blank=True)
    hunter_type = models.CharField(max_length=255, null=True, blank=True)
    stars = models.CharField(max_length=255, null=True, blank=True)
    time_limit = models.CharField(max_length=255, null=True, blank=True)
    fee = models.CharField(max_length=255, null=True, blank=True)
    reward = models.CharField(max_length=255, null=True, blank=True)
    hrp = models.CharField(max_length=255, null=True, blank=True)
    sub_goal = models.CharField(max_length=255, null=True, blank=True)
    sub_reward = models.CharField(max_length=255, null=True, blank=True)
    sub_hrp = models.CharField(max_length=255, null=True, blank=True)


