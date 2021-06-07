expression = input()
stack = []
for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        start_index = stack.pop()
        # махаме последния индекс от листа
        # и го запазваме в друга променлива
        print(expression[start_index: index + 1])
