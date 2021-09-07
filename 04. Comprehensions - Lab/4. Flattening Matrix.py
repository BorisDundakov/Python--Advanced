rows = int(input())
matrix = []
for el in range(rows):
    matrix.extend([int(el) for el in input().split(', ')])
print(matrix)

# print [(i, f) for i in nums for f in fruit if f[0] == "P" if i%2 == 1]