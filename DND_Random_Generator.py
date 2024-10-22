import randomname
import random

char_name = randomname.get_name()
char_name = char_name.replace('-' , ' ').title()

print(f'Your character name is: {char_name}')

#next stage is class selection

class_options = (
    'Barbarian',
    'Bard',
    'Cleric',
    'Druid',
    'Fighter',
    'Monk',
    'Paladin',
    'Ranger',
    'Rogue',
    'Sorceror',
    'Warlock',
    'Wizard',
)
char_class = random.choice(class_options)

print(f'Your character class is: {char_class}')

#next stage is background
background_options = (
    'Acoyte',
    'Criminal',
    'Sage',
    'Soldier',
    'Haunted One',
    'Criminal/Spy',
    'Folk Hero',
    'Noble',
    'Sage',
    'Soldier',
)

char_background = random.choice(background_options)

print(f'Your character background is: {char_background}')

#next stage is race/species
dwarf_race = ('Hill Dwarf' , 'Mountain Dwarf')
elf_race = ('High Elf' , 'Wood Elf' , 'Eladrin Elf')
halfling_race = ('Lightfoot Halfling' , 'Stout Halfling')
human_race = ('Human' , 'Variant Human')

race_options = ('Dragonborn' , 'Dwarf' , 'Elf' , 'Half-Elf' , 'Half-Orc' , 'Halfling' , 'Human' , 'Rock Gnome' , 'Tiefling' , 'Variant Aasimar')
char_race = random.choice(race_options)
if char_race == 'Dwarf':
    char_race = random.choice(dwarf_race)
elif char_race == 'Elf':
    char_race = random.choice(elf_race)
elif char_race == 'Halfling':
    char_race = random.choice(halfling_race)
elif char_race == 'Human':
    char_race = random.choice(human_race)

print(f'Your character\'s race is: {char_race}')

#next stage is Ability Score

def generate_ability_score():
    while True:
        char_str_pool = random.randint(0 , 7)
        char_str = char_str_pool + 8
        ab_pts_pool = 27 - char_str_pool

        char_dex_pool = random.randint(0 ,7)
        char_dex = char_dex_pool + 8
        ab_pts_pool -= char_dex_pool

        char_con_pool = random.randint(0 , 7)
        char_con = char_con_pool + 8
        ab_pts_pool -=  char_con

        char_int_pool = random.randint(0 , 7)
        char_int = char_int_pool + 8
        ab_pts_pool -= char_int_pool

        char_wis_pool = random.randint(0 , 7)
        char_wis = char_wis_pool + 8
        ab_pts_pool -= char_wis_pool

        char_cha_pool = random.randint(0 , 7)
        char_cha = char_cha_pool + 8
        ab_pts_pool -= char_cha_pool

        if ab_pts_pool == 0:
            return(char_str , char_dex , char_con , char_int , char_wis , char_cha , ab_pts_pool)

char_str, char_dex, char_con, char_int, char_wis, char_cha, ab_pts_pool = generate_ability_score()

print(f'Strength: {char_str}, Dexterity: {char_dex}, Constitution: {char_con}, Intelligence: {char_int}, Wisdom: {char_wis}, Charisma: {char_cha}')
print(f"Remaining Ability Points: {ab_pts_pool}")

#next stage is starting equipment
#TODO work on database for abilities based on the random picks of race/class to be able to proceed

#file__init.py this file tells python the folder executing in it is a module
#from.local import (function names) <== this would be the name of the other folders/files equipment or ability or class files that may be created 