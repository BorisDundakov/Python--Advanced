def age_assignment(*args, **kwargs):
    answer_dict = {}

    for name in args:
        letter = name[0]
        age = kwargs[letter]
        answer_dict[name] = age

    return answer_dict



print(age_assignment("Boris", "Peter", "Sam", S=36, P=22, B=61))
