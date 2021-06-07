sets_lenghts = [int(el) for el in input().split()]
first_set = set()
second_set = set()
for el in range(sets_lenghts[0]):
    first_set.add(int(input()))

for second_el in range(sets_lenghts[1]):
    second_set.add(int(input()))

result = first_set & second_set
# results 2 = first_set.intersection(second_set)
for el in result:
    print(el)



