import re

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
    parts = re.split(r'')

    command = input()