"""Serializers for MHAPI."""
from rest_framework import serializers
from Locations.models import Location
from Items.models import Weapon, Armor
from Monsters.models import Monster, Buff


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


class MonsterBuffSerializer(serializers.ModelSerializer):
    """Monster Buff Serializer for Monster Serializer."""

    class Meta:
        """Meta."""

        model = Buff
        fields = ['buff_type', 'initial', 'increase', 'dmax', 'duration', 'damage']


class MonsterSerializer(serializers.ModelSerializer):
    """Monster data."""

    weaknesses = MonsterBuffSerializer(many=True)

    class Meta:
        """Meta."""

        model = Monster

        fields = ['key', 'name', 'mclass', 'base_hp', 'weaknesses']
