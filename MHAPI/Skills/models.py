"""Skills models for MH Generations."""
from __future__ import unicode_literals

from django.db import models


class SkillTree(models.Model):
    """Skill Tree Model."""

    key = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)


class Skill(models.Model):
    """Skill Model."""

    key = models.CharField(max_length=255, null=True, blank=True)
    tree = models.ForeignKey(SkillTree, related_name='skills')
    name = models.CharField(max_length=255, null=True, blank=True)
    required_points = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
