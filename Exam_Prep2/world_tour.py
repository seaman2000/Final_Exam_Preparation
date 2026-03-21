def add_stop(stops:str, idx: int, stop: str):
    if 0 <= idx <= len(stops):
        return stops[:idx] + stop + stops[idx:]
    return stops

def remove_stop(stops: str, start: int, end: int):
    if 0 <= start <= end < len(stops):
        return stops[:start] + stops[end + 1:]
    return stops


def switch(stops:str , old:str , new: str):
    if old in stops:
        stops = stops.replace(old, new)
    return stops


all_stops = input()
command = input()

while command != "Travel":

    parts = command.split(":")
    type_of_command = parts[0]

    if type_of_command == "Add Stop":
        index = int(parts[1])
        current_stop = parts[2]
        all_stops = add_stop(all_stops, index, current_stop)
        print(all_stops)

    elif type_of_command == "Remove Stop":
        start_index = int(parts[1])
        end_index = int(parts[2])
        all_stops = remove_stop(all_stops, start_index, end_index)
        print(all_stops)

    elif type_of_command == "Switch":
        old_stop = parts[1]
        new_stop = parts[2]
        all_stops = switch(all_stops, old_stop, new_stop)
        print(all_stops)

    command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")