# Palm -> divisible by 3, but it is not divisible by 5
# Willow -> divisible by 5, but it is not divisible by 3
# Crosette -> divisible by both 3 and 5
from collections import deque

firework_effects = deque([int(num) for num in input().split(', ')])
explosive_power = deque([int(num) for num in input().split(', ')])
combination_sum = 0
firework_dict = {"palm": 0, "willow": 0, "crosette": 0}

for _ in range(len(firework_effects)):
    for _ in range(len(explosive_power) - 1, -1, -1):
        print(firework_effects[0] + explosive_power[-1])
        combination_sum = firework_effects[0] + explosive_power[-1]

        if firework_dict["palm"] and firework_dict["willow"] and firework_dict["crosette"] >= 3:
            print('Congrats! You made the perfect firework show!')
            for value in firework_dict.values():
                print(f'Palm Fireworks: {value[0]}')
                print(f'Willow Fireworks: {value[1]}')
                print(f'Crossette Fireworks: {value[2]}')
                break
            break

        if combination_sum % 3 == 0 and combination_sum % 5 != 0:
            firework_dict["palm"] += 1
            firework_effects.popleft()
            explosive_power.pop()
            firework_index = 0
            break

        elif combination_sum % 5 == 0 and combination_sum % 3 != 0:
            firework_dict["willow"] += 1
            firework_effects.popleft()
            explosive_power.pop()
            break

        elif combination_sum % 3 == 0 and combination_sum % 5 == 0:
            firework_dict["crosette"] += 1
            firework_effects.popleft()
            explosive_power.pop()
            break

        else:
            firework_effects[0] -= 1

            to_append = firework_effects.popleft()
            if to_append > 0:
                firework_effects.appendleft(to_append)

            break