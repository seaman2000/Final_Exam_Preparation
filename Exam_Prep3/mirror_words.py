import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

word_collection = {}
words = re.findall(pattern, text)
words_without_symbols = [w[1] for w in words]

if not words_without_symbols:
    print("No word pairs found!")
else:
    print(f"{len(words_without_symbols)} word pairs found!")
    for first, second in zip(words_without_symbols, words_without_symbols[1:]):
        if first == second[::-1]:
            word_collection[first] = second

if not word_collection:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    for first, second in word_collection.items():
        print(f"{first} <=> {second}", end=", ")


