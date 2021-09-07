nums = [float(el)for el in input().split()]


def round_line_func(number_list):
    res = [round(el)for el in number_list]
    return res


print(round_line_func(nums))