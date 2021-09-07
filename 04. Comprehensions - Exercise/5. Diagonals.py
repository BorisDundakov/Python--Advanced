matrix_size = int(input())
matrix = []
for _ in range(matrix_size):
    line = [int(el) for el in input().split(', ')]
    matrix.append(line)

first_diagonal = []
second_diagonal = []

for first_diag in range(len(matrix)):
    first_diagonal.append(matrix[first_diag][first_diag])

for row in range(len(matrix)):
    for col in range(len(matrix) - 1, -1, -1):
        second_diagonal.append(matrix[row][col])

        if row < len(matrix):
            row += 1
            continue
        break

    break

print(f'First diagonal: {", ".join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}')
