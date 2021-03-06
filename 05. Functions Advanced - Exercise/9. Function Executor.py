def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    results_list = []

    for func_definition in args:
        func, func_args = func_definition
        return_value = func(*func_args)
        results_list.append(return_value)

    return results_list


print(func_executor((sum_numbers, (4, 7)), (multiply_numbers, (2, 5))))
