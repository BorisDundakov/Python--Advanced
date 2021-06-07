command = input()
nums = [int(el) for el in input().split()]


def odd_even(word, numbers_list):
    result = []

    if word == 'Even':
        for el in range(len(numbers_list)):
            if numbers_list[el] % 2 == 0:
                result.append(numbers_list[el])
    else:
        for el in range(len(numbers_list)):
            if numbers_list[el] % 2 != 0:
                result.append(numbers_list[el])

    final = sum(result) * len(numbers_list)
    print(final)
    
odd_even(command, nums)
