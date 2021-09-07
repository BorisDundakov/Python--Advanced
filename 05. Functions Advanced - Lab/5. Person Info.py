def get_info(**kwargs):
    return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
# kwargs.get['name'] as an alternative

print(get_info(**{"name": "Peter", "town": "Sofia", "age": 20}))