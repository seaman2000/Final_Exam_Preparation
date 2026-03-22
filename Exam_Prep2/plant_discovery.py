import re

def rate(collection: dict, plant_type: str, rating: int):
    if plant_type not in collection:
        return False

    collection[plant_type][1].append(rating)
    return True


def update(collection: dict, plant_type: str, rarity: int):
    if plant_type not in collection:
        return False

    collection[plant_type][0] = rarity
    return True


def reset(collection: dict, plant_type: str):
    if plant_type not in collection:
        return False

    collection[plant_type][1] = []
    return True


number_of_lines = int(input())
plants = {}

for _ in range(number_of_lines):
    current_plant = input()
    plant, rarity = current_plant.split("<->")
    rarity = int(rarity)

    if plant not in plants:
        plants[plant] = [rarity, []]
    else:
        plants[plant][0] = rarity

command = input()
pattern = r'[A-Za-z]+|\d+'


while command != "Exhibition":
    parts = re.findall(pattern, command)
    type_of_command = parts[0]
    plant = parts[1]
    result = None

    if type_of_command == "Rate":
        rating = int(parts[2])
        result = rate(plants, plant, rating)

    elif type_of_command == "Update":
        new_rarity = int(parts[2])
        result = update(plants, plant, new_rarity)

    elif type_of_command == "Reset":
        result = reset(plants, plant)

    if not result:
        print("error")

    command = input()

print(f"Plants for the exhibition:")
for plant, values in plants.items():
    rarity, rating = values

    if len(rating) != 0:
        avg_rating = sum(rating) / len(rating)
    else:
        avg_rating = 0

    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")
