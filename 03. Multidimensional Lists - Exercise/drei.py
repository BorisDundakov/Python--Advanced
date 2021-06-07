rows, cols = [int(el) for el in input().split()]
matrix = []

for ind_row in range(rows):
    new_row = [int(el) for el in input().split()]
    matrix.append(new_row)

matrix_sum_res = []
this_sum = []
for row in range(rows - 1):
    for col in range(cols - 2):
        matrix_sum_res.extend([matrix[row][col]])




max_res = max(matrix_sum_res)
print(matrix_sum_res)
print(f'Sum = {max_res}')
print(this_sum)