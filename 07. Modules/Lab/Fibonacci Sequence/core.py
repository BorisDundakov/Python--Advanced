# such that each number is the sum of the two preceding ones,
# starting from 0 and 1
# F0 = 0, F1 = 1, F2 = 1, F3 = F1 + F2, F100 = F99 + F98


def create_sequence(count):
    solution_list = []
    for el in range(count):
        if el == 0:
            solution_list.append(0)
        elif el == 1:
            solution_list.append(1)
        else:
            solution_list.append((solution_list[-1] + solution_list[-2]))

    print(*solution_list)
    return solution_list


def locate(number, count):
    sequence = create_sequence(count)
    if number not in sequence:
        print(f"The number {number} is not in the sequence")
    else:
        for index in range(len(sequence)):
            if sequence[index] == number:
                print(f"The number - {number} is at index {index}")


locate(13, 10)
