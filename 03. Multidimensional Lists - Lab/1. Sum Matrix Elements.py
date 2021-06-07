matrixes_sizes = [int(el)for(el) in input().split(', ')]
matrix = []
matrix_sum = 0

for row in range(matrixes_sizes[0]):
    column_value = [int(el) for el in input().split(', ')]
    for col in range(len(column_value)):
        matrix.append(column_value)
        matrix_sum += sum(column_value)
        break

print(matrix_sum)
print(matrix)