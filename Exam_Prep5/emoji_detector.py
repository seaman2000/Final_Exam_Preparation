import re

text_with_emojis = input()

pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"

digits = re.findall(r"\d", text_with_emojis)

cool_threshold = 1

for digit in digits:
    cool_threshold *= int(digit)

cool_emojis = []
all_emojis = []
matches = re.finditer(pattern, text_with_emojis)

for match in matches:
    full_emoji = match.group(0)
    emoji = match.group(2)

    all_emojis.append(full_emoji)

    emoji_value = 0
    for char in emoji:
        emoji_value += ord(char)

    if emoji_value >= cool_threshold:
        cool_emojis.append(full_emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
print(f"{'\n'.join(cool_emojis)}")