"""Converting CSVs to Django Objects."""
from Items.models import Armor, Item
from Monsters.models import Monster, Buff
import csv


# Armor conversion


def armor_save(row):
    """Creating Armor objects."""
    armors = []
    for i in Item.objects.filter(item_type='Armor'):
        armors.append(i)
    if row[0] == '_id':
        print('header')
    else:
        for i in armors:
            if i.key == row[0]:
                name = i.name
                rarity = i.rarity
        to_save = Armor(name=name, key=row[0], rarity=rarity, slot=row[1],
                        defense=row[2], max_defense=row[3], fire_res=row[4],
                        thunder_res=row[5], dragon_res=row[6], water_res=row[7],
                        ice_res=row[8], gender=row[9], hunter_type=row[10], num_slots=row[11])
        to_save.save()


def run_csv_armor(csv_path):
    """Loop through armor csv file."""
    with open(csv_path, 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            armor_save(row)


# Monster Conversion

def monster_save(row):
    """Creating Monster Objects."""
    if row[0] == '_id':
        print('header')
    else:
        to_save = Monster(key=row[0], name=row[2], mclass=row[1], base_hp=row[8])
        to_save.save()


def run_csv_monster():
    """Loop though monster csv file."""
    with open('CSVs/monsters.csv', 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            monster_save(row)


def monster_status_save(row):
    """Create Monster Object."""
    if row[0] == "_id":
        print('header')
    else:
        monster_num = Monster.objects.get(key=row[1])
        to_save = Buff(monster=monster_num, key=row[0], buff_type=row[2], initial=row[3], increase=row[4], dmax=row[5], duration=row[6], damage=row[7])
        to_save.save()


def run_csv_mstatus():
    """Loop though status csv file."""
    with open('CSVs/monster_status.csv', 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            monster_status_save(row)
