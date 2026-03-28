coded_message = input()

command = input()
while command != "Finalize":
    parts = command.split()
    action = parts[0]

    if action == "Encrypt":
        coded_message = coded_message[::-1]
        print(coded_message)

    elif action == "Decrypt":
        result = ''
        for char in coded_message:
            if char.islower():
                result += char.upper()
            elif char.isupper():
                result += char.lower()
            else:
                result += char
        coded_message = result
        print(coded_message)

    elif action == "Substitute":
        old = parts[1]
        new = parts[2]
        if old not in coded_message:
            print("Character not found.")
        else:
            coded_message = coded_message.replace(old, new)
            print(coded_message)

    elif action == "Scramble":
        index = int(parts[1])
        char = parts[2]
        if 0 <= index < len(coded_message):
            coded_message = coded_message[:index] + char + coded_message[index + 1:]
            print(coded_message)
        else:
            print("Index out of bounds.")

    elif action == "Remove":
        substring = parts[1]
        if substring in coded_message:
            coded_message = coded_message.replace(substring, '')
        print(coded_message)


    else:
        print("Invalid command detected!")

    command = input()