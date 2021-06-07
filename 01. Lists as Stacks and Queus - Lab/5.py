children = [el for el in input().split()]
n = int(input())
for child in range(len(children)):
    if child == n:
        children.pop(children[child])
        print(children)

