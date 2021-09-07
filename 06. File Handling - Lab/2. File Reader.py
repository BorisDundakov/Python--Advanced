f = open('numbers.txt', 'w')
nums_sum = 0
for el in range(1, 6):
    f.writelines(str(el) + '\n')

f.close()

with open('numbers.txt') as n:
    print(sum(map(int, n.readlines())))
