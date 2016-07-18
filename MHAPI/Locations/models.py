"""Model for MHGen Locations."""
from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    """Location Model."""

    name = models.CharField(max_length=255)
    map_img = models.ImageField(upload_to='Images/Locations', default='01.png')
    key = models.CharField(max_length=15, null=True, blank=True)
