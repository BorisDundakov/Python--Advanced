
# TODO - 0/100 при judge, само zero tests минават

def numbers_searching(*numbers_queue):
    nums_count_dict = {}
    for el in numbers_queue:
        if el not in nums_count_dict:
            nums_count_dict[el] = 1
        else:
            nums_count_dict[el] += 1

    answer_list = []
    for key, value in nums_count_dict.items():
        if value >= 2:
            answer_list.append(key)

    answer_list.sort()

    missing_nums = sorted(set(range(answer_list[0], answer_list[-1])) - set(answer_list))
    missing_num = ''.join(str(missing_nums[0]))
    return [int(missing_num), answer_list]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
