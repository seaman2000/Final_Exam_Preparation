import re

text_with_emojis = input()

pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"

valid_emojis = re.findall(pattern, text_with_emojis)
valid_emojis = [item[1] for item in valid_emojis]

digits = re.findall(r"\d", text_with_emojis)

cool_threshold = 1

for digit in digits:
    cool_threshold *= int(digit)

cool_emojis = []
for emoji in valid_emojis:
    emoji_value = 0
    for char in emoji:
        emoji_value += ord(char)
    if emoji_value >= cool_threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
print(f"{'\n'.join(cool_emojis)}")