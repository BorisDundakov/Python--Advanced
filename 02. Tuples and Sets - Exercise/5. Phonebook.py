command = input()
kvp_phonebook = {}
while not command .isdigit():
    name, phone_number = command.split("-")
    if name not in kvp_phonebook:
        kvp_phonebook[name] = phone_number
    else:
        kvp_phonebook[name].update(phone_number)
    command = input()

success_contacts = []
for el in range(int(command)):
    for contact in kvp_phonebook:
        name_search = input()
        if name_search in contact:
            pass
            print(contact)
        else:
            print(f'Contact {name_search} does not exist.')


