nums_list = [int(el) for el in input().split()]


def even_numbers(numbers_list):
    result = list(filter(lambda x: x % 2 == 0, numbers_list))
    print(result)

even_numbers(nums_list)