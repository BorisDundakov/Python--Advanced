# start = int(input())
# end = int(input())
# divisble_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = []
# for el in range(start, end+1):
#     for ee in range(len(divisble_nums)):
#         if el % divisble_nums[ee] == 0:
#             res.append(el)
#             break
#
# print(res)

# for ee in range(len(divisble_nums))
# for el in range(start, end+1)

start = int(input())
end = int(input())
divisble_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
[res.append(el) for ee in range(len(divisble_nums)) for el in range(start, end + 1) if el % divisble_nums[ee] == 0]
print(list(set(res)))

print([num for num in range(start, end + 1) if [d for d in range(2, 11) if num % d == 0]])
