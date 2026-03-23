given_password = input()
command = input()

while command != "Done":
    parts = command.split()
    type_of_command = parts[0]

    if type_of_command == "TakeOdd":
        current_password = ""
        for idx in range(len(given_password)):
            if idx % 2 == 1:
                current_password += given_password[idx]
        given_password = current_password
        print(given_password)

    elif type_of_command == "Cut":
        index = int(parts[1])
        length = int(parts[2])
        given_password = given_password[:index] + given_password[index + length:]
        print(given_password)

    elif type_of_command == "Substitute":
        substring = parts[1]
        substitute = parts[2]
        if not substring in given_password:
            print("Nothing to replace!")
        else:
            given_password = given_password.replace(substring, substitute)
            print(given_password)

    command = input()

print(f"Your password is: {given_password}")
