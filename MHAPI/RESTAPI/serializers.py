"""Serializers for MHAPI."""
from rest_framework import serializers
from Locations.models import Location
from Items.models import Weapon, Armor


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for locations."""

    class Meta:
        """Meta."""

        model = Location

        fields = ['name', 'map_img', 'key']


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    """List name, key and type for each weapon."""

    class Meta:
        """Meta."""

        model = Weapon

        fields = ['name', 'key', 'wtype']


class WeaponSerializerHeavy(serializers.HyperlinkedModelSerializer):
    """All Weapon Data."""

    class Meta:
        """Meta."""

        model = Weapon

        fields = ['name', 'key', 'description', 'wtype', 'creation_cost', 'upgrade_cost', 
                    'attack', 'element', 'element_attack', 'element_2', 'element_2_attack',
                    'defense', 'affinity', 'horn_notes', 'shell_type', 'phial',
                    'charges', 'coating', 'recoil', 'reload_speed', 'rapid_fire',
                    'deviation', 'ammo', 'special_ammo', 'num_slots'
                    ]


class ArmorSerializer(serializers.HyperlinkedModelSerializer):
    """Armor Serializer."""

    class Meta:
        """Meta."""

        model = Armor

        fields = ['name', 'key', 'hunter_type', 'slot']


class ArmorSerializerHeavy(serializers.HyperlinkedModelSerializer):
    """All Armor Data."""

    class Meta:
        """Meta."""

        model = Armor

        fields = ['name', 'key', 'slot', 'rarity', 'defense', 'max_defense', 'fire_res',
                    'thunder_res', 'dragon_res', 'water_res', 'ice_res',
                    'gender', 'hunter_type', 'num_slots']
