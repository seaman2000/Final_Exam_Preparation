import re

text = input()

pattern = r'(#|\|)([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

matches = re.findall(pattern, text)

total_calories = 0

for match in matches:
    total_calories += int(match[3])

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for match in matches:
    item = match[1]
    date = match[2]
    calories = match[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")