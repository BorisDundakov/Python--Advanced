from collections import deque

# TODO: Optimize the code (use multiple functions, recusion etc.)


def list_manipulator(*kwargs):
    numbers_list = deque(kwargs[0])
    command_type = kwargs[1]



    def remove_add_last(numbers_list, *kwargs):
        if len(kwargs[1::]) == 2:

            if command_type == 'remove':
                if kwargs[2] == 'beginning':
                    numbers_list.popleft()
                    numbers_list = list(numbers_list)
                    return numbers_list
                else:
                    numbers_list.pop()
                    numbers_list = list(numbers_list)
                    return numbers_list
            else:
                if kwargs[2] == 'beginning':
                    numbers_list.appendleft(kwargs[3])
                    numbers_list = list(numbers_list)
                    return numbers_list
                else:
                    numbers_list.append(kwargs[3])
                    numbers_list = list(numbers_list)
                    return numbers_list
        else:
            n = kwargs[3]
            if kwargs[2] == 'beginning':
                for el in range(n):
                    numbers_list.popleft()

                numbers_list = list(numbers_list)
                return numbers_list

            else:
                for el in range(n):
                    numbers_list.pop()

                numbers_list = list(numbers_list)
                return numbers_list


    def remove_add_multiple(numbers_list, *kwargs):

        if kwargs[2] == 'beginning':
            numbers_list.extendleft([el for el in reversed(kwargs[3::])])
            numbers_list = list(numbers_list)
            return numbers_list

        elif kwargs[2] == 'end':
            numbers_list.extend(list(kwargs[3::]))
            numbers_list = list(numbers_list)
            return numbers_list


    if len(kwargs[1::]) == 2:

        return remove_add_last(*kwargs)
    else:
        return remove_add_multiple(*kwargs)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
