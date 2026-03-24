def contains(activation_key: str, sub: str):
    if sub in activation_key:
        return f"{activation_key} contains {substring}"
    return f"Substring not found!"


def flip_upper_and_lower(activation_key: str, upper_lower: str, start: int, end: int):
    sub_string = activation_key[start:end]
    if upper_lower == "Upper":
        sub_string = sub_string.upper()
    elif upper_lower == "Lower":
        sub_string = sub_string.lower()
    return activation_key[:start] + sub_string + activation_key[end:]


def slice_():
    pass



raw_activation_key = input()

command = input()
while command != "Generate":
    parts = command.split(">>>")
    action = parts[0]
    if action == "Contains":
        substring = parts[1]
        print(contains(raw_activation_key, substring))

    elif action == "Flip":
        upper_or_lower = parts[1]
        start_idx = int(parts[2])
        end_idx = int(parts[3])

    command = input()