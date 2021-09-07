from collections import deque

pizza_orders = deque([int(order) for order in input().split(', ')])
employee_capacity = deque([int(capacity) for capacity in input().split(', ')])
made_pizzas = []

COMPLETED = True

while True:

    if not 0 < pizza_orders[0] <= 10:
        pizza_orders.popleft()

    else:
        if pizza_orders[0] - employee_capacity[-1] <= 0:
            made_pizzas.append(pizza_orders[0])
            pizza_orders.popleft()
            employee_capacity.pop()
        else:
            pizza_orders[0] -= employee_capacity[-1]
            made_pizzas.append(employee_capacity[-1])
            employee_capacity.pop()


    if not pizza_orders:
        COMPLETED = True
        break

    if not employee_capacity:
        COMPLETED = False
        break

if COMPLETED:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {sum(made_pizzas)}')
    print(f'Employees: {", ".join([str(el) for el in employee_capacity])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(el) for el in pizza_orders])}')