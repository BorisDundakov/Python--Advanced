numbers = tuple([float(el) for el in input().split()])

numbers_dict = {}

for el in numbers:
    if el not in numbers_dict:
        numbers_dict[el] = 1
    else:
        numbers_dict[el] += 1

for key, value in numbers_dict.items():
    print(f'{key} - {value} times')
