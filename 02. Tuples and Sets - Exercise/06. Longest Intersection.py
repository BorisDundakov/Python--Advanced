import re

# intersection between two lists
n = int(input())
all_intersections = []

for el in range(n):
    command = input()
    res = re.split(',|-', command)
    first_start, first_end, second_start, second_end = [int(el) for el in res]

    first = []
    second = []

    for _ in range(first_start, first_end + 1):
        first.append(_)

    for _ in range(second_start, second_end + 1):
        second.append(_)

    first = set(first)
    second = set(second)
    all_intersections.append(list(first & second))

    first.clear()
    second.clear()

max_list = []

list_len = [len(i) for i in all_intersections]
for each in range(len(all_intersections)):
    if len(all_intersections[each]) == max(list_len):
        max_list = all_intersections[each]

print(f'Longest intersection is {max_list} with length {max(list_len)}')
