def insert_space(message:str, idx:int):
    message = message[:idx] + " " + message[idx:]
    return message


def reverse(message: str, sub_string: str):
    idx_of_sub = message.find(sub_string)
    message = message[:idx_of_sub] + sub_string[::-1]
    return message


def change_all(message: str, sub_string, new_string):
    new_message = message.replace(sub_string, new_string)
    return new_message


concealed_message = input()

command = input()
while command != "Reveal":
    parts = command.split(":|:")
    type_of_command = parts[0]

    if type_of_command == "InsertSpace":
        index = int(parts[1])
        concealed_message = insert_space(concealed_message, index)
        print(concealed_message)

    elif type_of_command == "Reverse":
        substring = parts[1]
        if substring not in concealed_message:
            print("error")
        else:
            concealed_message = reverse(concealed_message, substring)
            print(concealed_message)
    elif type_of_command == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        concealed_message = change_all(concealed_message, substring, replacement)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")