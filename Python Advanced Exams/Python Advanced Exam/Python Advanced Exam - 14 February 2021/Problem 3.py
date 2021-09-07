from collections import deque


def stock_availability(inventory_list, *parameter):
    answer_list = deque(inventory_list)
    if parameter[0] == 'delivery':
        answer_list.extend(parameter[1::])
    elif parameter[0] == 'sell':
        if len(parameter) == 1:
            answer_list.popleft()
        else:
            boxes_to_remove = parameter[1]
            if str(boxes_to_remove).isdigit():
                for el in range(boxes_to_remove):
                    answer_list.popleft()
            else:
                boxes_to_remove = parameter[1::]
                for item in list(answer_list):
                    if item in boxes_to_remove:
                        answer_list.remove(item)

    return list(answer_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "cookie"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

