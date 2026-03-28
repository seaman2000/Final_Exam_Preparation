import re

text = input()
pattern = r"[@#]+([a-z]{3,})[@#]+[^A-Za-z0-9]*/+(\d+)/+"

found_eggs = re.finditer(pattern, text)
for egg in found_eggs:
    print(f"You found {egg.group(2)} {egg.group(1)} eggs!")
