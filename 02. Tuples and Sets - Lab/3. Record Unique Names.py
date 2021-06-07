names_list = set()
n_names = int(input())

for el in range(n_names):
    names_list.add(input())

print('\n'.join(names_list))