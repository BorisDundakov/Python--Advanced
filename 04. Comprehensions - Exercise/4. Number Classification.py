positives, negatives, odd, even = ([] for i in range(4))
numbers_line = [int(num) for num in input().split(', ')]

[even.append(numbers_line[el]) for el in range(len(numbers_line))if numbers_line[el] % 2 == 0]
[odd.append(numbers_line[el]) for el in range(len(numbers_line))if numbers_line[el] % 2 != 0]
[positives.append(numbers_line[el]) for el in range(len(numbers_line))if numbers_line[el] >= 0]
[negatives.append(numbers_line[el]) for el in range(len(numbers_line))if numbers_line[el] < 0]

print(f'Positive: {", ".join(str(el) for el in positives)}')
print(f'Negative: {", ".join(str(el) for el in negatives)}')
print(f'Even: {", ".join(str(el) for el in even)}')
print(f'Odd: {", ".join(str(el) for el in odd)}')