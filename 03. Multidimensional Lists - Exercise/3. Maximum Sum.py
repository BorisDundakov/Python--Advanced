rows, cols = [int(el) for el in input().split()]
matrix = []

for ind_row in range(rows):
    new_row = [int(el) for el in input().split()]
    matrix.append(new_row)

current_sum = []
sums_list = []
for row in range(rows - 2):
    for col in range(cols - 2):
        a1 = matrix[row][col]
        a2 = matrix[row][col + 1]
        a3 = matrix[row][col + 2]
        b1 = matrix[row + 1][col]
        b2 = matrix[row + 1][col + 1]
        b3 = matrix[row + 1][col + 2]
        c1 = matrix[row + 2][col]
        c2 = matrix[row + 2][col + 1]
        c3 = matrix[row + 2][col + 2]
        current_sum.append([a1, a2, a3, b1, b2, b3, c1, c2, c3])

for el in current_sum:
    sums_list.append(sum(el))

res = max(sums_list)
print(f'Sum = {res}')
for el in current_sum:
    if sum(el) == res:
        for index in range(len(el)):
            if index == 3 or index == 6:
                print()
                print(el[index], end=' ')
            else:
                print(el[index], end=' ')
