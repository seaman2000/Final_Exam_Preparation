import re

places = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, places)

destinations = [match[1] for match in matches]

points = 0
for destination in destinations:
    points += len(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")