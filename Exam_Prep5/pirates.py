def plunder(target_cities:dict, current_town:str, killed_people:int, plundered_gold:int):
    target_cities[current_town][0] -= killed_people
    target_cities[current_town][1] -= plundered_gold
    if target_cities[current_town][0] <= 0 or target_cities[current_town][1] <= 0:
        del target_cities[current_town]
        return False
    return True


def prosper(target_cities: dict, current_town: str, gold_increase: int):
    if gold_increase < 0:
        return False
    target_cities[current_town][1] += gold_increase
    return True


command = input()

cities = {}
while command != "Sail":
    current_city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)

    if current_city not in cities:
        cities[current_city] = [population, gold]
    else:
        cities[current_city][0] += population
        cities[current_city][1] += gold
    command = input()

event = input()
while event != "End":

    parts = event.split("=>")
    action = parts[0]
    town = parts[1]

    if action == "Plunder":
        people = int(parts[2])
        gold = int(parts[3])
        result = plunder(cities, town, people, gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if not result:
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        gold = int(parts[2])
        result = prosper(cities, town, gold)
        if not result:
            print(f"Gold added cannot be a negative number!")
        else:
            total_gold = cities[town][1]
            print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")

    event = input()
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, values in cities.items():
        population, gold = values
        print(f"{city} -> Population: {population} citizens, Gold: {gold} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")