

def kwargs_length(**kwargs):
    counter = 0
    for el in range(len(kwargs)):
        counter += 1

    return counter


dictionary = {'name': 'Peter', 'age': 25, 'surname': 'Ivanov'}

print(kwargs_length(**dictionary))
