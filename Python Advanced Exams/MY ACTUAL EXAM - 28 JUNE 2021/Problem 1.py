from collections import deque

has_Failed = False
milkshakes = 0
Success = False
chocolates = deque([int(el) for el in input().split(', ')])
milk_cups = deque([int(el) for el in input().split(', ')])

while True:

    if milkshakes == 5:
        Success = True
        break

    if not milk_cups:
        Success = False
        break

    if not chocolates:
        Success = False
        break

    while milk_cups[0] <= 0:
        milk_cups.popleft()
        if not milk_cups:
            Success = False
            has_Failed = True
            break

    if not Success and has_Failed:
        break

    while chocolates[-1] <= 0:
        chocolates.pop()
        if not chocolates:
            Success = False
            has_Failed = True
            break

    if not Success and has_Failed:
        break

    if chocolates[-1] == milk_cups[0]:
        milkshakes += 1
        milk_cups.popleft()
        chocolates.pop()

    else:
        cup_to_remove = milk_cups.popleft()
        milk_cups.append(cup_to_remove)
        chocolates[-1] -= 5

if Success:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if sum(chocolates) != 0:
    print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
else:
    print("Chocolate: empty")

if sum(milk_cups) != 0:
    print(f"Milk: {', '.join([str(el) for el in milk_cups])}")

else:
    print("Milk: empty")