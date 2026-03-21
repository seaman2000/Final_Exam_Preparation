def rate(collection: dict, plant_type: str, rating: int):
    if plant_type not in collection:
        return "error"
    
    collection[plant_type][1].append(rating)


def update(collection: dict, plant_type: str, rarity: int):
    if plant_type not in collection:
        return "error"

    collection[plant_type][0] = rarity


def reset(collection: dict, plant_type: str):
    if plant_type not in collection:
        return "error"

    del collection[plant_type][1]




import re

number_of_lines = int(input())
plants = {}

for _ in range(number_of_lines):
    current_plant = input()
    plant, rarity = current_plant.split("<->")
    plants[plant] = int(rarity)

command = input()
pattern = r'[A-Za-z]+'

while command != "Exhibition":
    parts = re.findall(pattern, command)
    type_of_command = parts[0]
    plant = parts[1]

    if type_of_command == "Rate":
        rating = int(parts[2])
        plants = rate(plants, plant, rating)

    elif type_of_command == "Update":
        new_rarity = int(parts[2])
        plants = update(plants, plant, new_rarity)

    elif type_of_command == "Reset":
        plants = reset(plants, plant)
