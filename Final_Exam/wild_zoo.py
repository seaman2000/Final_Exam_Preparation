animals = {}

while True:
    command = input()
    if command == "EndDay":
        break
    parts = command.split(": ")
    action = parts[0]

    if action == "Add":
        name, needed_food, area = parts[1].split("-")
        needed_food = int(needed_food)
        if area not in animals:
            animals[area] = {}
        animals[area][name] = animals[area].get(name, 0) + needed_food

    elif action == "Feed":
        name, food = parts[1].split("-")
        food = int(food)
        for area, animal in animals.items():
            if name in animal:
                animal[name] -= food
                if animal[name] <= 0:
                    del animals[area][name]
                    print(f"{name} was successfully fed")
                break

print("Animals:")
for area, animal_food in animals.items():
    for animal, food in animal_food.items():
        print(f" {animal} -> {food}g")

print("Areas with hungry animals:")
for area, animals in animals.items():
    if animals:
        print(f"{area}: {len(animals.keys())}")


