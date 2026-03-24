def cast_spell():
    pass


def take_damage():
    pass


def recharge():
    pass


def heal():
    pass





number_of_heroes = int(input())

party = {}

for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    party[hero_name] = [int(hit_points), int(mana_points)]

command = input()
while command != "End":
    parts = command.split(" – ")
    action = parts[0]
    current_hero = parts[1]

    if action == "CastSpell":
        pass
    elif action == "TakeDamage":
        pass
    elif action == "Recharge":
        pass
    elif action == "Heal":
        pass


    command = input()