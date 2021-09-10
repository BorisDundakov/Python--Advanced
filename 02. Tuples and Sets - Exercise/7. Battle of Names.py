n = int(input())
names = []
evens = []
odds = []
for el in range(1, n + 1):
    name = input()
    for each_letter in range(len(name)):
        names.append(ord(name[each_letter]))

    if sum(names) // el % 2 == 0:
        evens.append(sum(names) // el)
    else:
        odds.append(sum(names) // el)

    names.clear()

set_sum_evens = set(evens)
set_sum_odds = set(odds)

if sum(evens) == sum(odds):
    print(f', '.join([str(el) for el in set_sum_evens.union(set_sum_odds)]))
elif sum(odds) > sum(evens):
    print(f', '.join([str(el) for el in set_sum_odds.difference(set_sum_evens)]))
else:
    print(f', '.join([str(el) for el in set_sum_odds.symmetric_difference(set_sum_evens)]))