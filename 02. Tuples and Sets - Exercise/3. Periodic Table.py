count_lines = int(input())
periodic_table_set = set()
for el in range(count_lines):
    command = input().split()
    for element in range(len(command)):
        periodic_table_set.add(command[element])

for el in periodic_table_set:
    print(el)

