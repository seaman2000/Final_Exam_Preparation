import re

places = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, places)

destinations = [match[1] for match in matches]


print(destinations)