def add(dictionary, piece_, composer_, key_):
    if piece_ in dictionary:
        return f"{piece_} is already in the collection!"
    else:
        dictionary[piece_] = (composer_, key_)
        return f"{piece_} by {composer_} in {key_} added to the collection!"

def remove(dictionary, piece_):
    if piece_ in dictionary:
        del dictionary[piece_]
        return f"Successfully removed {piece_}!"
    else:
        return f"Invalid operation! {piece_} does not exist in the collection."


def change_key(dictionary, piece_, key_new):
    if piece_ in dictionary:
        dictionary[piece_][1] = key_new
        return f"Changed the key of {piece_} to {key_new}"
    else:
        return f"Invalid operation! {piece_} does not exist in the collection."


number_of_pieces = int(input())

compositions = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    compositions[piece] = (composer, key)

command = input()
while command != "End":

    command = command.split("|")
    type_of_command = command[0]
    piece = command[1]

    if type_of_command == "Add":
        composer = command[2]
        key = command[3]
        add(compositions, piece, composer, key)

    elif type_of_command == "Remove":
        remove(compositions, piece)

    elif type_of_command == "ChangeKey":
        new_key = command[2]
        change_key(compositions, piece, new_key)



    command = input()