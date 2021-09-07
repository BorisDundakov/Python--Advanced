numbers_dictionary = {}

line = input()

while line != "Search":
    numbers_as_string = line
    try:
        number = int(input())
        numbers_dictionary[numbers_as_string] = number
    except ValueError:
        print("The variable number must be an integer")


    finally:
        line = input()

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    finally:
        line = input()

print(numbers_dictionary)
