


command = input()
while command != "Statistics":
    parts = command.split("=")
    action = parts[0]
    if action == "Add":
        username = parts[1]
        sent = parts[2]
        received = parts[3]
    elif action == "Message":
        sender = parts[1]
        receiver = parts[2]
    elif action == "Empty":
        username = parts[1]