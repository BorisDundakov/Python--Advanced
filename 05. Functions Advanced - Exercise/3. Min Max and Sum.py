initial_line = [int(el) for el in input().split()]


def min_max_sum(line):
    min_sum = min(line)
    max_sum = max(line)
    line_sum = sum(line)
    print(f'The minimum number is {min_sum}')
    print(f'The maximum number is {max_sum}')
    print(f'The sum number is: {line_sum}')


min_max_sum(initial_line)