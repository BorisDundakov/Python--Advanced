from collections import deque

# TODO: NEW and improved version for Github

food_quantity_available = int(input())
start_food_quantity = food_quantity_available
orders = deque(int(el) for (el) in input().split())
print(max(orders))
completed = True
counter = 0

for each_order in orders:
    if food_quantity_available - each_order >= 0:
        food_quantity_available -= each_order
        counter += 1
        continue

    elif start_food_quantity >= food_quantity_available:
        for el in range(counter):
            orders.popleft()

    if orders:
        print(f'Orders left: {" ".join([str(el) for el in orders])}')
        completed = False
    break

if completed:
    print('Orders complete')