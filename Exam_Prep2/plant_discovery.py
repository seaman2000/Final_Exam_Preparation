def rate():
    pass


def update():
    pass


def reset():
    pass




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
        pass
    elif type_of_command == "Update":
        pass
    elif type_of_command == "Reset":
        pass
