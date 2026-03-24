def plunder():
    pass


def prosper():
    pass


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

event = input()
while event != "End":
    parts = event.split("=>")
    action = parts[0]
    town = parts[1]

    if action == "Plunder":
        pass
    elif action == "Prosper":
        pass

    event = input()
