# matrix_size = int(input())
# matrix = [[0] * matrix_size for i in range(matrix_size)]
# print(matrix)
saved_coordinates = [0, 0]
n = int(input())
matrix = []
for line in range(n):
    input_row = [el for el in input()]
    matrix.append([i for i in input_row])

has_Broken = False
command = input()
while True:
    if command == 'left':
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                # I think this is correct...
                if matrix[row][col] == 'S':
                    if col - 1 > -1:
                        matrix[row][col - 1] = 'S'
                        matrix[row][col] = '.'
                        continue
                    else:
                        has_Broken = True
                        print(matrix)
                        break

    elif command == 'right':
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                # I think this is correct...
                if matrix[row][col] == 'S':
                    if col + 1 < len(matrix):
                        matrix[row][col + 1] = 'S'
                        matrix[row][col] = '.'
                        continue
                    else:
                        has_Broken = True
                        print(matrix)
                        break
    elif command == 'down':
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                # I think this is correct...
                if matrix[row][col] == 'S':
                    if row + 1 < len(matrix):
                        matrix[row + 1][col] = '.'
                        matrix[row][col] = '.'
                        continue
                    else:
                        has_Broken = True
                        print(matrix)
                        break
    elif command == 'up':
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                # I think this is correct...
                if matrix[row][col] == 'S':
                    if row - 1 < -1:
                        matrix[row - 1][col] = '.'
                        matrix[row][col] = '.'
                        continue
                    else:
                        has_Broken = True
                        print(matrix)
                        break

    command = input()
