given_password = input()
command = input()
current_password = ""

while command != "Done":
    parts = command.split()
    type_of_command = parts[0]

    if type_of_command == "TakeOdd":
        for idx in range(len(given_password)):
            if idx % 2 == 1:
                current_password += given_password[idx]
        print(current_password)

    elif type_of_command == "Cut":
        index = int(parts[1])
        length = int(parts[2])
        current_password = current_password[:index] + current_password[index + length:]
        print(current_password)

    elif type_of_command == "Substitute":
        substring = parts[1]
        substitute = parts[2]
        if not substring in current_password:
            print("Nothing to replace!")
        else:
            current_password = current_password.replace(substring, substitute)
            print(current_password)

    command = input()

print(f"Your password is: {current_password}")
