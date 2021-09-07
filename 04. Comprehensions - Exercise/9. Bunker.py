# bunker_items = {category: {} for category in input().split(', ')}
# n = int(input())
# bunker_dict = {}
# total_quantity = 0
# total_quality = 0
# for el in range(n):
#     category, item_name, item_params = input().split(' - ')
#     quantity, quality = item_params.split(';')
#     qt, number_quanity = quantity.split(':')
#     total_quantity += int(number_quanity)
#     ql, number_quality = quality.split(':')
#     total_quality += int(number_quality)
#     if category not in bunker_dict:
#         bunker_dict[category] = [item_name]
#     else:
#         bunker_dict[category].append(item_name)
#
# print(f'Count of items: {total_quantity}')
# print(f"Average quality: {total_quality / len(bunker_dict) :.2f}")
#
# for key, value in bunker_dict.items():
#     print(f'{key} -> {", ".join(value)}')


categories = {category: [] for category in input().split(", ")}

quantity = 0
quality = 0

for _ in range(int(input())):
     data = input().split(" - ")
     categories[data[0]].append(data[1])

     information_data = data[2].split(";")
     quantity += int(information_data[0].split(":")[1])
     quality += int(information_data[1].split(":")[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {quality / len(categories):.2f}")
[print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]