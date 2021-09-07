from collections import deque


def math_operations(*args, **kwargs):
    args_list = list(args)
    kwargs_dict = kwargs
    for el in range(len(args_list)):
        counter = el
        if el == len(args_list) + 1:
            counter = 0

        elif el > len(args_list) + 1:
            counter = abs(len(args_list) + 1 - el)

        # докато съм в листа
        if counter + 1 == 1:
            kwargs_dict['a'] += args_list[counter]
        elif counter + 1 == 2:

            kwargs_dict['s'] -= args_list[counter]
        elif counter + 1 == 3:
            try:
                res = kwargs_dict['d'] / args_list[counter]
                kwargs_dict['d'] = res
                # args_list[counter] / kwargs_dict['d']
            except:
                args_list.remove(args_list[counter])

        elif counter + 1 == 4:
            kwargs_dict['m'] *= args_list[counter - 1]
            args_list = deque(args_list)
            args_list.popleft()
            args_list.popleft()
            args_list.popleft()

            el = 0

    return kwargs_dict


print(math_operations(6, a=0, s=0, d=0, m=0))
