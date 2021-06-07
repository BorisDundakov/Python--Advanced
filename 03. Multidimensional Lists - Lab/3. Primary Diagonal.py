size = int(input())
matrix = []
primary_diagonal = 0
for el in range(size):
    matrix.append([int(num) for num in input().split()])

counter = 0
for el in range(size):
    primary_diagonal += matrix[counter][counter]
    counter += 1

print(primary_diagonal)