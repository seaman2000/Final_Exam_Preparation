def plunder(target_cities:dict, current_town:str, killed_people:int, plundered_gold:int):
    target_cities[current_town][0] -= killed_people
    target_cities[current_town][1] -= plundered_gold
    if target_cities[current_town][0] <= 0 or target_cities[current_town][1] <= 0:

        del target_cities[current_town]
        return (f"{current_town} plundered! {plundered_gold} gold stolen, {killed_people} citizens killed.\n"
                f"{current_town} has been wiped off the map!")

    return f"{current_town} plundered! {plundered_gold} gold stolen, {killed_people} citizens killed."



def prosper(target_cities: dict, current_town: str, gold_increase: int):
    if gold_increase < 0:
        return f"Gold added cannot be a negative number!"
    target_cities[current_town][1] += gold_increase
    total_gold = target_cities[current_town][1]
    return f"{gold_increase} gold added to the city treasury. {current_town} now has {total_gold} gold."


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
        print(plunder(cities, town, people, gold))

    elif action == "Prosper":
        gold = int(parts[2])
        print(prosper(cities, town, gold))

    event = input()

print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
for city, values in cities.items():
    population, gold = values
    print(f"{city} -> Population: {population} citizens, Gold: {gold} kg")