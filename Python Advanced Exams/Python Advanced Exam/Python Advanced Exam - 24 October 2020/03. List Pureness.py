from collections import deque

# TODO -> 40/100 in Judge


def best_list_pureness(*args):

    numbers_list = deque(args[-2])
    k = args[-1]

    rotation_results = []
    final_res = []

    for el in range(k + 1):
        for index in range(len(numbers_list)):
            rotation_results.append(numbers_list[index] * index)

        final_res.append(sum(rotation_results))
        a = numbers_list.pop()
        numbers_list.appendleft(a)
        rotation_results.clear()

    return f"Best pureness {max(final_res)} after {final_res.index(max(final_res))} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

