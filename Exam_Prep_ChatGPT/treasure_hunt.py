def loot(collection_of_treasures:list, looted: list ):
    looted = looted[::-1]
    for item in looted:
        if item not in collection_of_treasures:
            collection_of_treasures.insert(0, item)


def drop(collection_of_treasures:list, idx:int):
    if 0 <= idx < len(collection_of_treasures):
        match = collection_of_treasures.pop(idx)
        collection_of_treasures.append(match)


def steal(collection_of_treasures: list, count:int):
        stolen_items = collection_of_treasures[-count:]
        collection_of_treasures = collection_of_treasures[:-count]
        return collection_of_treasures, stolen_items



treasures = input().split("|")
command = input()
while command != "Yohoho!":
    parts = command.split()
    action = parts[0]

    if action == "Loot":
        looted_items = parts[1:]
        loot(treasures, looted_items)

    elif action == "Drop":
        index = int(parts[1])
        drop(treasures, index)

    elif action == "Steal":
        count = int(parts[1])
        treasures, stole_items = steal(treasures,count)
        if stole_items:
            print(f"{', '.join(stole_items)}")

    command = input()

if treasures:
    sum_of_items_len = sum(len(i) for i in treasures)
    avg_credits = sum_of_items_len / len(treasures)
    print(f"Average treasure gain: {avg_credits:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

