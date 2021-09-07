rows, cols = [int(el) for el in input().split()]
matrix = []
for el in range(rows):
    matrix.append([el for el in input().split()])

command = input()

while command != "END":
    split_command = command.split()
    if split_command[0] == "swap":

        try:
            split_command[1] = int(split_command[1])
            split_command[2] = int(split_command[2])
            split_command[3] = int(split_command[3])
            split_command[4] = int(split_command[4])
        except:
            print('Invalid input!')
            command = input()
            continue

        if len(split_command) != 5:
            print('Invalid input!')
            command = input()


        elif split_command[1] > rows or split_command[2] > rows:

            print('Invalid input!')
            command = input()
            continue

        elif split_command[1] < 0 or split_command[2] < 0:

            print('Invalid input!')
            command = input()
            continue


        elif split_command[3] > cols or split_command[4] > cols:

            print('Invalid input!')
            command = input()
            continue

        elif split_command[3] < 0 or split_command[4] < 0:

            print('Invalid input!')
            command = input()
            continue

        for ind_row in range(rows):
            for ind_col in range(cols):
                ind_1 = matrix[split_command[1]][split_command[2]]
                matrix[split_command[1]][split_command[2]] = matrix[split_command[3]][split_command[4]]
                matrix[split_command[3]][split_command[4]] = ind_1

                for line in range(len(matrix)):
                    print(' '.join(matrix[line]))

                break
            break
        command = input()

    else:
        print('Invalid input!')
        command = input()