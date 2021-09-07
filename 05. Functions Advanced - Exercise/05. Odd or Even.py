command = input()
nums = [int(el) for el in input().split()]


def odd_even(word, numbers_list):
    result = []
    for el in range(len(numbers_list)):
        if word == 'Even':
            result = list(filter(lambda number: number % 2 == 0, numbers_list))
            continue
        else:
            result = list(filter(lambda number: number % 2 != 0, numbers_list))
            continue

    final = sum(result) * len(numbers_list)
    print(final)


odd_even(command, nums)
