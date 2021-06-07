def concatenate(*args):
    result = []
    for el in range(len(args)):
        result.append(args[el])
    return ''.join(result)


print(concatenate("Soft", "Uni", "Is", "Great", "!"))