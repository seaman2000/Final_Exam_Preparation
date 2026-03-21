def add_stop():
    pass


def remove_stop():
    pass


def switch():
    pass


all_stops = input()
command = input()

while command != "Travel":

    command = input()
    parts = command.split(":")
    type_of_command = parts[0]

    if type_of_command == "Add Stop":
        index = int(parts[1])
        current_stop = parts[2]

    elif type_of_command == "Remove Stop":
        start_index = int(parts[1])
        end_index = int(parts[2])

    elif type_of_command == "Switch":
        old_stop = parts[1]
        new_stop = parts[2]