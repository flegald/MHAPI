"""Converting CSVs to Django Objects."""
from Items.models import Armor
from Items.models import Item
import csv


def armor_save(row):
    """Creating Armor objects."""
    armors = []
    for i in Item.objects.filter('Armor'):
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
