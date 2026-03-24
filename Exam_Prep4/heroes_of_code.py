def cast_spell(heroes:dict, hero: str, mana: int, spell: str):
    if heroes[hero][1] >= mana:
        heroes[hero][1] -= mana
        mana_left = heroes[hero][1]
        return f"{hero} has successfully cast {spell} and now has {mana_left} MP!"
    return f"{hero} does not have enough MP to cast {spell}!"


def take_damage(heroes:dict, hero:str, dmg: int, attacker: str):
    heroes[hero][0] -= dmg
    current_hp = heroes[hero][0]
    if heroes[hero][0] > 0:
        return f"{hero} was hit for {dmg} HP by {attacker} and now has {current_hp} HP left!"
    del heroes[hero]
    return f"{hero} has been killed by {attacker}!"


def recharge(heroes: dict, hero: str, mana_recharge:int):
    last_mana = heroes[hero][1]
    heroes[hero][1] += mana_recharge
    if heroes[hero][1] > 200:
        heroes[hero][1] = 200
    amount_recovered = heroes[hero][1] - last_mana
    return f"{hero} recharged for {amount_recovered} MP!"


def heal(heroes: dict, hero:str, hp_recovery: int):
    last_hp = heroes[hero][0]
    heroes[hero][0] += hp_recovery
    if heroes[hero][0] > 100:
        heroes[hero][0] = 100
    hp_recovered = heroes[hero][0] - last_hp
    return f"{hero} healed for {hp_recovered} HP!"


number_of_heroes = int(input())

party = {}

for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    party[hero_name] = [int(hit_points), int(mana_points)]

command = input()

while command != "End":
    parts = command.split(" - ")
    action = parts[0]
    current_hero = parts[1]

    if action == "CastSpell":
        needed_mana_points = int(parts[2])
        spell_name = parts[3]
        print(cast_spell(party, current_hero, needed_mana_points, spell_name))

    elif action == "TakeDamage":
        damage = int(parts[2])
        attacker = parts[3]
        print(take_damage(party, current_hero, damage, attacker))

    elif action == "Recharge":
        amount_of_mana = int(parts[2])
        print(recharge(party, current_hero, amount_of_mana))

    elif action == "Heal":
        amount_of_heal = int(parts[2])
        print(heal(party, current_hero, amount_of_heal))


    command = input()

for hero, values in party.items():
    hp, mana = values
    print(f"{hero}\n"
    f"  HP: {hp}\n"
    f"  MP: {mana}")