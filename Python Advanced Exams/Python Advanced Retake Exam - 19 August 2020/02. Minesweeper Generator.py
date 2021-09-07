from collections import deque

n = int(input())
matrix = []
for line in range(n):
    input_row = [0] * n
    matrix.append([i for i in input_row])

n_bombs = int(input())
coordinates = deque(input())
coordinates = list(coordinates)
for row in range(n):
    for col in range(n):
        if row == int(coordinates[1]) and col == int(coordinates[4]):
            matrix[row][col] = '*'
            if row and col == n - 1:
                break
            coordinates = deque(input())
            coordinates = list(coordinates)

print(matrix)

for row in range(n):
    for col in range(n):
        # up, down, left, right, diag up_left, diag up_right, diag down_left, diag down_right

        # down
        if row + 1 < n:
            if matrix[row + 1][col] == '*':
                matrix[row][col] += 1

        # right
        if col + 1 < n:
            if matrix[row][col + 1] == '*':
                matrix[row][col] += 1

        # left
        if col - 1 <= 0:
            if matrix[row][col - 1] == '*':
                matrix[row][col] += 1

        # up
        if row - 1 <= 0:
            if matrix[row - 1][col] == '*':
                matrix[row][col] += 1

        # diag down_right

        if row + 1 < n and col + 1 < n:
            if matrix[row + 1][col + 1] == '*':
                matrix[row][col] += 1

        # diag up_right
        if row - 1 <= 0 and col + 1 < n:
            if matrix[row - 1][col + 1] == '*':
                matrix[row][col] += 1

        # diag up_left
        if row + 1 < n and col - 1 <= 0:
            if matrix[row + 1][col - 1] == '*':
                matrix[row][col] += 1

        # diag down_left
        if row - 1 <= 0 and col - 1 <= 0:
            if matrix[row - 1][col - 1] == '*':
                matrix[row][col] += 1


        print(matrix)
print(matrix)