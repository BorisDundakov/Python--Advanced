def print_first_half(size):
    for row in range(1, size + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


def print_second_half(size):
    for row in range(size - 1, 0, -1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


def print_triangle(size):
    print_first_half(size)
    print_second_half(size)


if __name__ == '__main__':
    print('Not from here')
