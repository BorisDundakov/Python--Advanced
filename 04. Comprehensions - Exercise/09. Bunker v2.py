item_categories = [el for el in input().split(', ')]
n = int(input())
bunker = {}
total_quantity = 0
for el in range(n):
    command = input().split(' - ')
    if command[0] not in bunker:
        bunker[command[0]] = [command[1]]
    else:
        bunker[command[0]].append(command[1])

    for digit in command[2]:
        if digit.isdigit():
            total_quantity += int(digit)

print(bunker)
print(total_quantity)
