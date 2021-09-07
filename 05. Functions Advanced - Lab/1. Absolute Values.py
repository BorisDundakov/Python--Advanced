nums = [float(el) for el in input().split()]


def convert_num_to_abs(nums_list):
    result = [abs(el) for el in nums_list]
    return result


print(convert_num_to_abs(nums))