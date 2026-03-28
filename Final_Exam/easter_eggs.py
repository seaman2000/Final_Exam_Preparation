import re

text = input()
pattern = r"(?:(?<=\s)|[@#]){1,}([a-z]{3,})[@#]{1,}(?:[^|A-Za-z0-9])*/{1,}(\d+)\b"

found_eggs = re.finditer(pattern, text)
for egg in found_eggs:
    print(f"You found {egg.group(2)} {egg.group(1)} eggs!")
