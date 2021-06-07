from collections import deque

my_list = []
are_Remaining = True
name = input()

while not name == "End":
    if not name == "Paid":
        my_list.append(name)
        are_Remaining = True
        name = input()

    else:
        for each_el in my_list:
            print(each_el)
        my_list.clear()
        are_Remaining = False
        name = input()

if are_Remaining:
    print(f"{len(my_list)} people are remaining.")