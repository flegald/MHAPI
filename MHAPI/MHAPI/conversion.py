"""Converting CSVs to Django Objects."""
from Locations.models import Location
from Items.models import Armor, Item
from Monsters.models import Monster, Buff, Damage, Habitat, Weakness
from Quests.models import Quest
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


def monster_damage_save(row):
    """Create Monster Damage Object."""
    if row[0] == '_id':
        print('header')
    else:
        monster_num = Monster.objects.get(key=row[1])
        to_save = Damage(monster=monster_num, key=row[0], body_part=row[2], 
                        cut=row[3], impact=row[4], shot=row[5], fire=row[6], 
                        water=row[7], ice=row[8], thunder=row[9], dragon=row[10], 
                        ko=row[10])
        to_save.save()


def run_csv_damage():
    """Loop through monster damage csv file."""
    with open('CSVs/monster_damage.csv') as ifile:
        data = csv.reader(ifile)
        for row in data:
            monster_damage_save(row)


def monster_habitat_save(row):
    """Create Habitat Object."""
    if row[0] == '_id':
        print('header')
    else:
        monster_num = Monster.objects.get(key=row[1])
        location_num = Location.objects.get(key=row[2])
        to_save = Habitat(monster=monster_num, location=location_num, start_area=row[3],
                            move_area=row[4], rest_area=row[5])
        to_save.save()


def run_csv_habitat():
    """Loop Through habitat csv file."""
    with open('CSVs/monster_habitat.csv', 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            monster_habitat_save(row)


def yes_or_no(col):
    """Return a yes or no value from a 1 or 0 entry in csv."""
    if col == '1':
        return 'Yes'
    else:
        return 'No'


def lo_to_hi(col):
    """Return a None to High value for a 0123 entry in csv."""
    if col == '3':
        return 'High'
    elif col == '2':
        return 'Mid'
    elif col == '1':
        return 'Low'
    else:
        return 'None'


def monster_weakness_save(row):
    """Create Weakness Object."""
    if row[0] == '_id':
        print('header')
    else:
        monster_num = Monster.objects.get(key=row[1])
        fire = lo_to_hi(row[3])
        water = lo_to_hi(row[4])
        thunder = lo_to_hi(row[5])
        ice = lo_to_hi(row[6])
        dragon = lo_to_hi(row[7])
        poison = lo_to_hi(row[8])
        para = lo_to_hi(row[9])
        sleep = lo_to_hi(row[10])
        pitfall = yes_or_no(row[11])
        shock = yes_or_no(row[12])
        flash = yes_or_no(row[13])
        sonic = yes_or_no(row[14])
        dung = yes_or_no(row[15])
        meat = yes_or_no(row[16])
        to_save = Weakness(monster=monster_num, state=row[2], fire=fire, water=water, thunder=thunder,
                            ice=ice, dragon=dragon, poison=poison, para=para, sleep=sleep,
                            pitfall_trap=pitfall, shock_trap=shock, flash_bomb=flash,
                            sonic_bomb=sonic, dung_bomb=dung, meat=meat)
        to_save.save()


def run_weakness_csv():
    """Loop through weakness csv."""
    with open('CSVs/monster_weakness.csv', 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            monster_weakness_save(row)


def ailments(row):
    """Add ailments to Monster Model."""
    if row[0] == '_id':
        print('header')
    else:
        monster = Monster.objects.get(key=row[1])
        if not monster.ailments:
            monster.ailments = [row[2]]
        else:
            monster.ailments.append(row[2])
        monster.save()


def ailments_csv():
    """Loop trought ailments csv."""
    with open('CSVs/monster_ailments.csv', 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            ailments(row)

# Quests


def return_quest_type(quest):
    """Quest type."""
    if quest == '1':
        return 'Key'
    elif quest == '2':
        return 'Urgent'
    else:
        return ''


def return_hunter_type(quest):
    """Palico quest or not."""
    if quest == '1':
        return 'Palico'
    else:
        return ''


def return_goal_type(quest):
    """Get goal type."""
    if quest == '3':
        return 'Gathering'
    elif quest == '2':
        return 'Capture'
    else:
        return 'Slaying'


def get_location(quest):
    """Return Location Object."""
    return Location.objects.get(key=quest)


def quests_save(row):
    """Create Quest Object."""
    if row[0] == '_id':
        print('header')
    else:
        location = get_location(row[9])
        qtype = return_quest_type(row[4])
        qhunter_type = return_hunter_type(row[7])
        qgoal_type = return_goal_type(row[6])
        to_save = Quest(key=row[0], name=row[1], location=location, goal=row[2], hub=row[3], qtype=qtype,
                        rank=row[5], goal_type=qgoal_type, hunter_type=qhunter_type,
                        stars=row[8], time_limit=row[10], fee=row[11], reward=row[12], hrp=row[13],
                        sub_goal=row[14], sub_reward=row[15], sub_hrp=row[16])
        to_save.save()


def run_quest_csv():
    """Loop through quests csv."""
    with open('CSVs/quests.csv', 'rb') as ifile:
        data = csv.reader(ifile)
        for row in data:
            quests_save(row)
