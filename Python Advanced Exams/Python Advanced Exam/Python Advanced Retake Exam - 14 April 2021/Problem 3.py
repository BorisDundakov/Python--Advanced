def flights(*args):
    all_args = args[0::]
    flights_dict = {}

    for el in range(len(all_args)):
        if all_args[el] == 'Finish':
            return flights_dict
        if all_args[el] not in flights_dict:
            if not str(all_args[el]).isdigit():
                flights_dict[all_args[el]] = 0

    return flights_dict
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))