from collections import deque

#
# def math_operations(*args, **kwargs):
#     final_dictionary = {}
#     args_list = list(args)
#     kwargs_dict = kwargs
#     counter = 0
#     for el in range(len(args_list)):
#         counter = el
#         if el == len(args_list) + 1:
#             el = 0
#
#         # докато съм в листа
#         if counter + 1 == 1:
#             kwargs_dict['a'] += args_list[counter]
#         elif counter + 1 == 2:
#             kwargs_dict['s'] -= args_list[counter]
#         elif counter + 1 == 3:
#             try:
#                 args_list[counter] / kwargs_dict['d']
#             except:
#                 args_list.remove(args_list[counter])
#         elif counter + 1 == 4:
#             kwargs_dict['m'] *= args_list[counter]
#             args_list = deque(args_list)
#             args_list.popleft()
#             args_list.popleft()
#             args_list.popleft()
#             args_list.popleft()
#
#             el = 0
#
#     return kwargs_dict
#
#
# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(6, a=0, s=0, d=0, m=0))


from collections import deque


def math_operations(*args, **kwargs):
    counter = 1
    numbers = deque(args)

    while numbers:
        num = numbers.popleft()
        if counter == 5:

            counter = 1
            numbers.appendleft(num)

        elif counter == 1:
            kwargs["a"] += num

            counter += 1

        elif counter == 2:
            kwargs["s"] -= num

            counter += 1

        elif counter == 3:
            if num != 0:
                kwargs["d"] /= num

            counter += 1

        elif counter == 4:
            kwargs["m"] *= num
            counter += 1

    return kwargs

print(math_operations(6, a=0, s=0, d=0, m=0))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))