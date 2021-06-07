row, col = [int(el) for el in input().split(', ')]
matrix = []
for entry in range(row):
    matrix.append([int(num) for num in input().split()])

answer_sum = 0
for current_column in range(col):
    for current_row in range(row):
        answer_sum += matrix[current_row][current_column]
    print(answer_sum)
    answer_sum = 0