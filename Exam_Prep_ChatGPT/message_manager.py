def add(messages:dict, name:str, sent:int, received:int):
    if name not in messages:
        messages[name] = [sent, received]


def message(messages:dict, sender:str, receiver:str, cap:int):
    if sender in messages and receiver in messages:
        messages[sender][0] += 1
        messages[receiver][1] += 1
        if messages[sender][0] + messages[sender][1] >= cap:
            del messages[sender]
            return True
        elif messages[receiver][0] + messages[receiver][1] >= cap:
            del messages[receiver]
            return True
    return False

def empty():
    pass

capacity = int(input())
message_manager = {}
command = input()
while command != "Statistics":
    parts = command.split("=")
    action = parts[0]
    if action == "Add":
        username = parts[1]
        sent = int(parts[2])
        received = int(parts[3])

    elif action == "Message":
        sender = parts[1]
        receiver = parts[2]
        if message(message_manager, sender, receiver, capacity):
            print(f"{sender} reached the capacity!")

    elif action == "Empty":
        username = parts[1]