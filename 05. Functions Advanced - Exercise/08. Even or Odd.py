def even_odd(*args):
    nums = []
    res = []

    for el in range(len(args)):
        if args[el] != "odd" and args[el] != "even":
            nums.append(args[el])
            continue
        else:
            if args[el] != "odd":
                for ele in range(len(nums)):
                    if nums[ele] % 2 == 0:
                        res.append(nums[ele])
            else:
                for ele in range(len(nums)):
                    if nums[ele] % 2 != 0:
                        res.append(nums[ele])


    return res


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))