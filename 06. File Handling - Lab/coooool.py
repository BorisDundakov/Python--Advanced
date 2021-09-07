with open('direct_print_file.txt', 'w') as f:
    for i in range(11):
        print(str(i), file=f)  # print function works in file, not in console
