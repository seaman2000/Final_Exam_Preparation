def add(collection, piece_, composer_, key_):
    if piece_ in collection:
        return f"{piece_} is already in the collection!"

    collection[piece_] = [composer_, key_]
    return f"{piece_} by {composer_} in {key_} added to the collection!"


def remove(collection, piece_):
    if piece_ in collection:
        del collection[piece_]
        return f"Successfully removed {piece_}!"

    return f"Invalid operation! {piece_} does not exist in the collection."


def change_key(collection, piece_, key_new):
    if piece_ in collection:
        collection[piece_][1] = key_new
        return f"Changed the key of {piece_} to {key_new}!"

    return f"Invalid operation! {piece_} does not exist in the collection."


number_of_pieces = int(input())

compositions = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    compositions[piece] = [composer, key]

command = input()
while command != "Stop":

    parts = command.split("|")
    type_of_command = parts[0]
    piece = parts[1]

    if type_of_command == "Add":
        composer = parts[2]
        key = parts[3]
        print(add(compositions, piece, composer, key))

    elif type_of_command == "Remove":
        print(remove(compositions, piece))

    elif type_of_command == "ChangeKey":
        new_key = parts[2]
        print(change_key(compositions, piece, new_key))

    command = input()

for piece, values in compositions.items():
    composer, key = values
    print(f"{piece} -> Composer: {composer}, Key: {key}")