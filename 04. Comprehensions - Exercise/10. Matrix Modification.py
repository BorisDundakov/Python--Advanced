matrix_rows = int(input())
matrix = []
for el in range(matrix_rows):
    matrix.append([int(e) for e in input().split()])

command = input()

while command != 'END':
    split_command = command.split()
    row = int(split_command[1])
    col = int(split_command[2])
    val = int(split_command[3])

    if not 0 <= row <= len(matrix) - 1:
        print('Invalid coordinates')
        command = input()
        continue

    if not 0 <= col <= len(matrix) - 1:
        print('Invalid coordinates')
        command = input()
        continue

    if split_command[0] == 'Add':
        matrix[row][col] += val

    elif split_command[0] == 'Subtract':
        matrix[row][col] -= val

    command = input()

c = 0
for line in matrix:
    for val in line:
        c += 1
        if c == matrix_rows:
            c = 0
            print(val, end=' ')
            print()

            continue
        print(val, end=' ')