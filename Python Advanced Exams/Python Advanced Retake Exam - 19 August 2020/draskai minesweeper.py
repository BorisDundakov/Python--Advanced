from collections import deque

n = int(input())
matrix = []
for line in range(n):
    input_row = [0] * n
    matrix.append([i for i in input_row])

n_bombs = int(input())
coordinates = deque(input())
coordinates = list(coordinates)
has_broken = False

for row in range(n):
    if has_broken:
        break
    for col in range(n):
        if row == int(coordinates[1]) and col == int(coordinates[4]):
            matrix[row][col] = '*'
            coordinates = deque(input())
            coordinates = list(coordinates)
            continue


print(matrix)