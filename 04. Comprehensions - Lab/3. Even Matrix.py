rows = int(input())
matrix = []
for el in range(rows):
    matrix.append([int(el) for el in input().split(', ') if int(el) % 2 == 0])
print(matrix)

