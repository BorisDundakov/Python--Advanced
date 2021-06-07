number_of_guests = int(input())
reservations = set()
VIP_Guests = set()
Regular_Guests = set()
for el in range(number_of_guests):
    reservation_input = input()
    reservations.add(reservation_input)

command = input()
while not command == 'END':
    if command in reservations:
        reservations.remove(command)

    command = input()
print(len(reservations))
for el in reservations:
    if el[0].isdigit():
        VIP_Guests.add(el)
    else:
        Regular_Guests.add(el)

VIP_Guests = set(sorted(VIP_Guests))
Regular_Guests = set(sorted(Regular_Guests))
print('\n'.join(sorted(VIP_Guests.union(Regular_Guests))))
