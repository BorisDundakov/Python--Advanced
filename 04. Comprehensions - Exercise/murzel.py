first_split = input()
answer = []
for el in first_split:
    for e in el:
        if e != ' ':
            answer.append(e)
finale = []
reversing = []
for a in range(len(answer) - 1, -1, -1):
    if answer[a] != "|":
        reversing.append(answer[a])
        continue
    reversing.reverse()
    finale += reversing
    reversing.clear()

reversing.reverse()
finale += reversing
for el in finale:
    if el.isdigit():
        print(el, end=' ')