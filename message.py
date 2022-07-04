import random

def get_message(name, receiver):
    subject = f'Secret Santa Assigned to {name}'
    message = f"<font size='+1'><b>You received {receiver} for Secret Santa!</b><br><br>Some rules: <ul><li>Do not tell others who you have for Secret Santa</li><li>Spend $20 or less on the gift</li><li>Wrap the gift in a gift bag instead of wrapping paper (since people might be able to tell who wrapped the gift)</li></ul></font>"
    return [subject, message]


def get_random_person(receivers):
    number = random.randint(0, len(receivers) - 1)
    return receivers[number]


def get_messages(names):
    receivers = list(names.keys())
    result = {}
    for name in names.keys():
        receiver = get_random_person(receivers)
        if [name] == [receiver]:
            return get_messages(names)
        while receiver == name:
            receiver = get_random_person(receivers)
        receivers.remove(receiver)
        result[name] = get_message(name, receiver)

    return result
        
