size = int(input())
matrix = []

for row in range(size):
    symbols = input()
    matrix.append([el for el in symbols])

search_symbol = input()

answer_row = 0
answer_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == search_symbol:
            answer_col = col
            answer_row = row

res = any(search_symbol in entry for entry in matrix)
if res:
    print(f'({answer_row}, {answer_col})')
else:
    print(f'{search_symbol} does not occur in the matrix')