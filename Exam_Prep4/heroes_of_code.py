number_of_heroes = int(input())

party = {}

for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    party[hero_name] = [int(hit_points), int(mana_points)]
    