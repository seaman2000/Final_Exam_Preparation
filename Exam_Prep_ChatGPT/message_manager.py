def add(messages:dict, name:str, sent:int, received:int):
    if name not in messages:
        messages[name] = [sent, received]


def message(messages:dict, sender:str, receiver:str, cap:int):
    sender_above_cap = False
    receiver_above_cap = False
    if sender in messages and receiver in messages:
        messages[sender][0] += 1
        messages[receiver][1] += 1
        if messages[sender][0] + messages[sender][1] >= cap:
            del messages[sender]
            sender_above_cap = True
        if messages[receiver][0] + messages[receiver][1] >= cap:
            del messages[receiver]
            receiver_above_cap = True
    return sender_above_cap, receiver_above_cap

def empty(messages:dict, user:str):
    if user == "All":
        messages.clear()
    elif user in messages:
        del messages[user]

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
        add(message_manager, username, sent, received)

    elif action == "Message":
        sender = parts[1]
        receiver = parts[2]
        sender_full, receiver_full = message(message_manager, sender, receiver, capacity)
        if sender_full:
            print(f"{sender} reached the capacity!")
        if receiver_full:
            print(f"{receiver} reached the capacity!")

    elif action == "Empty":
        username = parts[1]
        empty(message_manager, username)
    command = input()

print(f"Users count: {len(message_manager)}")
for user, values in message_manager.items():
    print(f"{user} - {sum(values)}")