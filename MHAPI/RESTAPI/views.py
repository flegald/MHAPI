"""REST views."""
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from RESTAPI.serializers import LocationSerializer, WeaponSerializer, WeaponSerializerHeavy, ArmorSerializer, ArmorSerializerHeavy, MonsterSerializer, MonsterSerializerSingle

from Locations.models import Location
from Items.models import Weapon, Armor
from Monsters.models import Monster, Buff


# Locations
class LocationListView(ListAPIView):
    """Display List of all Locations."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def list(self, request, *args, **kwargs):
        """Return List of all locations."""
        return super(LocationListView, self).list(request, *args, **kwargs)


@api_view()
def LocationSingleView(request, *args, **kwargs):
    """Display Single Location."""

    filter_by = kwargs['name']
    to_show = Location.objects.get(name=filter_by)
    img_link = to_show.map_img._get_url()
    img_link = 'http://localhost:8000' + img_link
    return Response({'Name': to_show.name, 'Key': to_show.key, 'Link To Map Image': img_link})


# Weapons

class WeaponListView(ListAPIView):
    """List Weapon name, key and type."""

    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def list(self, request, *args, **kwargs):
        """Return list."""
        return super(WeaponListView, self).list(request, *args, **kwargs)


class HeavyWeaponListView(ListAPIView):
    """Display List of all Weapon Data."""

    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializerHeavy

    def list(self, request, *args, **kwargs):
        """Return list."""
        return super(HeavyWeaponListView, self).list(request, *args, **kwargs)


@api_view()
def WeaponSingleView(request, *args, **kwargs):
    """Display Single Weapon Details."""

    filter_by = kwargs['name']
    to_show = Weapon.objects.get(name=filter_by)
    aff = to_show.affinity + '%'
    return Response({'Name': to_show.name,
                        'Key': to_show.key,
                        'Description': to_show.description,
                        'Weapon Type': to_show.wtype,
                        'Attack': to_show.attack,
                        'Creation Cost': to_show.creation_cost,
                        'Upgrade Cost': to_show.upgrade_cost,
                        'Element': to_show.element,
                        'Element Attack': to_show.element_attack,
                        'Element 2': to_show.element_2,
                        'Element 2 Attack': to_show.element_2_attack,
                        'Defense': to_show.defense,
                        'Affinity': aff,
                        'Horn Notes': to_show.horn_notes,
                        'Shell Type': to_show.shell_type,
                        'Phial': to_show.phial,
                        'Charges': to_show.charges,
                        'Coating': to_show.coating,
                        'Recoil': to_show.recoil,
                        'Reload Speed': to_show.reload_speed,
                        'Rapid Fire': to_show.rapid_fire,
                        'Deviation': to_show.deviation,
                        'Ammo': to_show.ammo,
                        'Special Ammo': to_show.special_ammo,
                        'Number of Slots': to_show.num_slots,
                    })

# Armor


class ArmorListView(ListAPIView):
    """List Armor name, key, hunter_type and slot."""

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

    def list(self, request, *args, **kwargs):
        """Return list."""
        return super(ArmorListView, self).list(request, *args, **kwargs)


class ArmorListViewHeavy(ListAPIView):
    """List all Armor Data."""

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializerHeavy

    def list(self, request, *args, **kwargs):
        """Return list."""
        return super(ArmorListViewHeavy, self).list(request, *args, **kwargs)


@api_view()
def ArmorSingleView(request, *args, **kwargs):
    """Display Armor Weapon Details."""

    filter_by = kwargs['name']
    to_show = Armor.objects.get(name=filter_by)
    return Response({'Name': to_show.name,
                    'Key': to_show.key,
                    'Slot': to_show.slot,
                    'Rarity': to_show.rarity,
                    'Defense': to_show.defense,
                    'Max Defense': to_show.max_defense,
                    'Fire Res': to_show.fire_res,
                    'Thunder Res': to_show.thunder_res,
                    'Dragon Res': to_show.dragon_res,
                    'Water Res': to_show.water_res,
                    'Ice Res': to_show.ice_res,
                    'Gender': to_show.gender,
                    'Hunter Type': to_show.hunter_type,
                    'Num Slots': to_show.num_slots})

# Monsters


class MonsterListView(ListAPIView):
    """List Monster Data."""

    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

    def list(self, request, *args, **kwargs):
        """Return list."""
        return super(MonsterListView, self).list(request, *args, **kwargs)


class MonsterSingleView(RetrieveAPIView):
    """List Single Monster."""

    queryset = Monster.objects.all()
    lookup_field = 'name'
    serializer_class = MonsterSerializerSingle

    def get(self, request, *args, **kwargs):
        """Get out Single Monster."""
        filter_by = kwargs['name']
        self.queryset = self.queryset.filter(name=filter_by)
        return super(MonsterSingleView, self).get(request, *args, **kwargs)

