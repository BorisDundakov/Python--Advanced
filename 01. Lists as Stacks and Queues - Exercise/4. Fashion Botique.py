stack_of_clothes = [int(el) for el in input().split()]
rack_capacity = int(input())
loaded_stack = []
sum_box_clothes = sum(stack_of_clothes)
rack_counter = 0
while sum(loaded_stack) < sum_box_clothes:
    if len(loaded_stack) == 0:
        loaded_stack.append(stack_of_clothes[0])
        rack_counter += 1
        continue
    for el in range(len(stack_of_clothes)):
        if loaded_stack + stack_of_clothes[el] < rack_capacity:
            loaded_stack += stack_of_clothes[el]
            if sum(loaded_stack) >= sum_box_clothes:
                break

        else:
            loaded_stack.append(stack_of_clothes[el])
            rack_counter += 1



print(rack_counter)