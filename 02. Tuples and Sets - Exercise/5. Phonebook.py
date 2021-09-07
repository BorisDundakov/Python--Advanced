phonebook = {}
command = input()

while not command.isdigit():
    name, phone_number = command.split('-')
    phonebook[name] = phone_number
    command = input()

for contact in range(int(command)):
    contact_name = input()
    if contact_name in phonebook:
        print(f'{contact_name} -> {phonebook[contact_name]}')
    else:
        print(f'Contact {contact_name} does not exist.')