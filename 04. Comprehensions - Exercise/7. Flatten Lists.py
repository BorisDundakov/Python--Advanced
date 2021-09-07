# elements = input().split()
# reversed_lst = []
# second_split = ' '.join(elements).split('|')
#
# for el in range(len(second_split) - 1, -1, -1):
#     reversed_lst.append(second_split[el])
#
# for el in reversed_lst:
#     print(el.strip(), end=' ')


numbers = [[element for element in sequence.split(" ")
            if element.lstrip("+-").isdigit()]
           for sequence in input().split("|")]
numbers.reverse()
numbers = [number for sequence in numbers for number in sequence]
print(" ".join(str(x) for x in numbers))