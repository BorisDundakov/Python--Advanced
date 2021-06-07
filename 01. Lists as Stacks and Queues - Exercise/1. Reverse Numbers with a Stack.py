# reverse list
# numbers = [int(el) for el in input().split()]
# for el in range(len(numbers), 0, -1):
#     print(el, end=" ")
#
# # reverse stack

word_nums = input().split()
result = []

while len(word_nums) > 0:
    result.append(word_nums.pop())

print(' '.join(result))
