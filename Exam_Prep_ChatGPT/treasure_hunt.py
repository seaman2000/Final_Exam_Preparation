def loot(collection_of_treasures:list, looted: list ):
    for item in looted:
        if item not in collection_of_treasures:
            collection_of_treasures.insert(0, item)


def drop(collection_of_treasures:list, idx:int):
    if 0 <= idx < len(collection_of_treasures):
        matched_item = collection_of_treasures[idx]
        collection_of_treasures.remove(matched_item)
        collection_of_treasures.append(matched_item)


def steal(collection_of_treasures: list, count:int):
    if 0 < count < len(collection_of_treasures):
        counted_items = collection_of_treasures[-1:(-count)+1: -1]
        collection_of_treasures = collection_of_treasures[-1:(-count) + 1: -1]
        return collection_of_treasures, counted_items
    return None


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
        if steal(treasures, count) is not None:
            treasures, stole_items = steal(treasures,count)
            print(f"{', '.join(stole_items)}")





