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


def slice_(activation_key: str, start: int, end: int):
    activation_key = activation_key[:start] + activation_key[end:]
    return activation_key


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
        raw_activation_key = flip_upper_and_lower(raw_activation_key, upper_or_lower, start_idx, end_idx)
        print(raw_activation_key)

    elif action == "Slice":
        start_idx = int(parts[1])
        end_idx = int(parts[2])
        raw_activation_key = slice_(raw_activation_key, start_idx, end_idx)
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")