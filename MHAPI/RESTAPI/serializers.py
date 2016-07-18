"""Serializers for MHAPI."""
from rest_framework import serializers
from Locations.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for locations."""

    class Meta:
        """Meta."""

        model = Location

        fields = ['name', 'map_img', 'key']
