heroes_names = input().split(', ')
inventory = {}
hero_item = {}
command = input()
total_cost = 0

while command != 'End':
    split_command = command.split('-')
    name = split_command[0]
    item = split_command[1]
    cost = int(split_command[2])

    if name not in heroes_names:
        command = input()
        continue

    if name not in inventory:
        total_cost = 0
        total_cost += cost
        inventory[name] = cost
        hero_item[name] = [item]

    else:
        if item not in hero_item[name]:
            hero_item[name].append(item)
            total_cost += cost
            inventory[name] = total_cost

    command = input()

for key, value in inventory.items():
    print(f'{key} -> Items: {len(hero_item[key])}, Cost: {value}')