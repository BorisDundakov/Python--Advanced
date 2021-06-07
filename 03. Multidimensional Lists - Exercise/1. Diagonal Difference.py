matrix_size = int(input())
matrix = []
for row in range(matrix_size):
    input_row = [int(el) for el in input().split()]
    matrix.append(input_row)

primary_diagonal = 0
secondary_diagonal = 0

for row in range(matrix_size):
    for col in range(matrix_size):
        if row == col:
            primary_diagonal += matrix[row][col]

max_column = matrix_size - 1

for row in range(matrix_size):
    secondary_diagonal += matrix[row][max_column]
    max_column -= 1



print(abs(primary_diagonal - secondary_diagonal))
