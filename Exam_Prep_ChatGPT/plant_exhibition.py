import re

def rate(collection: dict, plant:str, rating:int,) -> bool:
    if plant in collection:
        collection[plant][1] += rating
        return True
    else:
        return False


def update(collection:dict, plant:str, rarity:int) -> bool:
    if plant in collection:
        collection[plant] = rarity
        return True
    else:
        return False


def reset(collection: dict, plant:str):
    if plant in collection:
        collection[plant][1] = []
        return True
    else:
        return False


number_of_plants = int(input())
plants_collection = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    if plant not in plants_collection:
        plants_collection[plant] = [int(rarity), []]
    else:
        plants_collection[plant][0] = int(rarity)

command = input()
while command != "Exhibition":
    parts = re.split(r"[:\s\-]+", command)
    action = parts[0]
    plant = parts[1]
    wrong_plant = False

    if action == "Rate":
        rating = int(parts[2])
        if not rate(plants_collection, plant, rating):
            wrong_plant = True
            
    elif action == "Update":
        rarity = int(parts[2])
        if not update(plants_collection, plant, rarity):
            wrong_plant = True

    elif action == "Reset":
        if not reset(plants_collection, plant):
            wrong_plant = True

    if wrong_plant:
        print("error")
    command = input()