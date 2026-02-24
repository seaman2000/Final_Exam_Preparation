def move(letters_number: int, message:list) -> list:
    return message[letters_number:] + message[:letters_number]


def insert(idx: int, value_: str, message:list) -> list:
    message.insert(idx, value_)
    return message


def change_all(substring, replacement, message):
    return [replacement if letter == substring else letter for letter in message]


encrypted_message = input()
encrypted_message = list(encrypted_message)

while True:
    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {''.join(encrypted_message)}")
        break

    parts = command.split("|")

    if parts[0] == "Move":
        number_of_letters = int(parts[1])
        encrypted_message = move(number_of_letters, encrypted_message)

    elif parts[0] == "Insert":
        index = int(parts[1])
        value = parts[2]
        encrypted_message = insert(index, value, encrypted_message)

    elif parts[0] == "ChangeAll":
        substr = parts[1]
        replace = parts[2]
        encrypted_message = change_all(substr, replace, encrypted_message)


