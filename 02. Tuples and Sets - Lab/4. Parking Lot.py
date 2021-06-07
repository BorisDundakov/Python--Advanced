n_commands = int(input())
set_reg_plates = set()
for el in range(n_commands):
    command, reg_plate = input().split(', ')
    if command == 'IN':
        set_reg_plates.add(reg_plate)
    elif command == 'OUT':
        set_reg_plates.remove(reg_plate)
    else:
        continue

if not set_reg_plates:
    print('Parking Lot is Empty')
else:
    print('\n'.join([el for el in set_reg_plates]))
