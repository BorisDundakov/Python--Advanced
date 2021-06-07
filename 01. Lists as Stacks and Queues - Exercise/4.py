stack_of_clothes = [int(el) for el in input().split()]
rack_capacity = int(input())

number_of_racks = 1
current_rack_weight = 0

for i in range(len(stack_of_clothes)):
    current_clothing_item = stack_of_clothes.pop()

    if current_clothing_item + current_rack_weight > rack_capacity:
        number_of_racks += 1
        current_rack_weight = 0

    current_rack_weight += current_clothing_item

print(number_of_racks)