def enter():
    print("Enter your mathematical operation below:")

    first_number, sign, second_number = input().split()
    return first_number, sign, second_number


def check_first_num(first_num):
    try:
        number_1 = float(first_num)
        return number_1
    except ValueError:
        raise ValueError("Please enter a correct value for the first number!")


def check_second_num(second_num):
    try:
        number_2 = int(second_num)
        return number_2
    except ValueError:
        raise ValueError("Please enter a correct value for the second number!")


def check_sign(first_number, sign, second_number):
    if sign == "/":
        return print(check_first_num(first_number) / check_second_num(second_number))
    elif sign == "*":
        return print(check_first_num(first_number) * check_second_num(second_number))
    elif sign == "+":
        return print(check_first_num(first_number) + check_second_num(second_number))
    elif sign == "-":
        return print(check_first_num(first_number) - check_second_num(second_number))

    else:
        raise ValueError("Please enter a correct sign ( +, -, /,  or *)")

