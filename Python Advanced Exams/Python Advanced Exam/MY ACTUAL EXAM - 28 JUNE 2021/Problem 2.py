matrix = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),}

for row in range(5):
    matrix.append(input().split())

n_commands = int(input())
starting_pos = []
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 'A':
            starting_pos.append([row, col])

for el in range(n_commands):
    if el == 0:
        position = starting_pos
    command = input().split()
    if command[0] == 'shoot':
       for direction in directions:
           next_row = row + directions[direction][0]
           next_col = row + directions[direction][1]

    elif command[0] == 'move':
        pass
