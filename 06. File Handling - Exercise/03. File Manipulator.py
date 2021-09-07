import os

line = input()
while not line == 'End':
    command, *args = line.split('-')

    if command == 'Create':
        with open(args[0], 'w'):
            pass

    elif command == 'Add':
        filename, line = args[0], args[1]
        with open(filename, 'a') as file:
            file.write(line + '\n')

    elif command == 'Replace':
        filename, old, new = args
        try:
            with open(filename, 'r') as file:
                content = file.read()

            with open(filename, 'w+') as file:
                content = content.replace(old, new)
                file.write(content)



        except Exception as e:
            print('An error has occured')
            line = input()
            continue

    elif command == 'Delete':
        try:
            os.remove(args[0])
        except FileNotFoundError:
            print('An error has occured')

    line = input()
