import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

word_collection = []
words = re.findall(pattern, text)
words_without_symbols = [(first, second) for _, first, second in words]

if not words_without_symbols:
    print("No word pairs found!")
else:
    print(f"{len(words_without_symbols)} word pairs found!")
    for (first, second) in words_without_symbols:
        if first == second[::-1]:
            word_collection.append(f"{first} <=> {second}")

if not word_collection:
    print(f"No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(word_collection))



