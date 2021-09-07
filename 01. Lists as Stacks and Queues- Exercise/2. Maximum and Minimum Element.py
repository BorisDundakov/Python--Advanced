from collections import deque

n = int(input())
my_queries = deque()
for el in range(n):
    command = input()

    if '1' in command:
        split_command = command.split()
        my_queries.append(int(split_command[1]))

    elif command == '2':
        if len(my_queries) > 0:
            my_queries.pop()


    elif command == '3':
        if len(my_queries) > 0:
            print(max(my_queries))

    elif command == '4':
        if len(my_queries) > 0:
            print(min(my_queries))


print(', '.join([str(el) for el in reversed(my_queries)]))