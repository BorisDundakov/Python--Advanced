from collections import deque

customers_list = deque([int(el) for el in input().split(', ')])
taxis_list = deque([int(el) for el in input().split(', ')])
res = []
for customer in range(len(customers_list)):
    for taxi in range(len(taxis_list) - 1, -1, -1):
        if taxis_list[taxi] - customers_list[customer] >= 0:
            res.append(customers_list[customer])
            customers_list.popleft()
            taxis_list.pop()
            continue
        taxis_list.pop()

if not customers_list:
    print('All customers were driven to their destinations')
    print(f'Total time: {sum(res)} minutes')
else:
    print('Not all customers were driven to their destinations')
    customers_list = list(customers_list)
    print(f'Customers left: '+', '.join([str(el) for el in customers_list]))