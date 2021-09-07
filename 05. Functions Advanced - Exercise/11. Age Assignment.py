def age_assignment(*args, **kwargs):
    first_letters = []
    names = []
    final_dict = {}
    first_letter_name_dict = {}
    for el in range(len(args)):
        names.append(args[el])

    for first_letter in names:
        first_letters.append(first_letter[0])

    for letter in first_letters:
        for name in names:
            if name[0] == letter:
                first_letter_name_dict[letter] = name

    for key_kw, value_kw in kwargs.items():
        for key_fl, value_fl in first_letter_name_dict.items():
            if key_kw == key_fl:
                key_kw = value_fl
                final_dict[value_fl] = value_kw

    return final_dict


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))