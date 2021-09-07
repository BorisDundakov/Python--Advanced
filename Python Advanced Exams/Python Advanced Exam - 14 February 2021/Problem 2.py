size = int(input())
matrix = []
total_points = 0
coordinates_list = []
Game_Over = False
for el in range(size):
    matrix.append(input().split())
for row in range(len(matrix)):
    if Game_Over:
        break
    for col in range(len(matrix)):
        if matrix[row][col] == 'P':
            while not Game_Over:
                if total_points >= 100:
                    break

                command = input()
                if command == 'right':
                    if col + 1 <= size:
                        if matrix[row][col + 1].isdigit:
                            coordinates_list.append([row, col + 1])
                            val = (matrix[row][col + 1])
                            col = col + 1
                            total_points += int(val)

                        elif matrix[row][col + 1] == 'X':
                            total_points = total_points // 2
                            print(f"Game over! You've collected {total_points} coins.")
                            Game_Over = True
                            break

                    else:
                        total_points = total_points // 2
                        print(f"Game over! You've collected {total_points} coins.")
                        Game_Over = True
                        break

                elif command == 'left':
                    if col - 1 >= 0:
                        if matrix[row][col - 1].isdigit():
                            coordinates_list.append([row, col - 1])
                            val = (matrix[row][col - 1])
                            col = col - 1
                            total_points += int(val)

                        elif matrix[row][col - 1] == 'X':
                            total_points = total_points // 2
                            print(f"Game over! You've collected {total_points} coins.")
                            Game_Over = True
                            break

                    else:
                        total_points = total_points // 2
                        print(f"Game over! You've collected {total_points} coins.")
                        Game_Over = True
                        break


                elif command == 'up':
                    if row - 1 >= 0:
                        if matrix[row - 1][col].isdigit():
                            coordinates_list.append([row - 1, col])
                            val = (matrix[row - 1][col])
                            row = row - 1
                            total_points += int(val)

                        elif matrix[row - 1][col] == 'X':
                            total_points = total_points // 2
                            print(f"Game over! You've collected {total_points} coins.")
                            Game_Over = True
                            break
                    else:
                        total_points = total_points // 2
                        print(f"Game over! You've collected {total_points} coins.")
                        Game_Over = True
                        break

                elif command == 'down':
                    if row + 1 <= size:
                        if matrix[row + 1][col].isdigit():
                            coordinates_list.append([row + 1, col])
                            val = (matrix[row + 1][col])
                            row = row + 1

                            total_points += int(val)

                        elif matrix[row + 1][col] == 'X':
                            total_points = total_points // 2
                            print(f"Game over! You've collected {total_points} coins.")
                            Game_Over = True
                            break
                    else:
                        total_points = total_points // 2
                        print(f"Game over! You've collected {total_points} coins.")
                        Game_Over = True
                        break

if not Game_Over:
    print(f"You won! You've collected {total_points} coins.")
print('Your path:')
for el in coordinates_list:
    print(el)