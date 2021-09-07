import math

first_num = int(input())
base = input()

try:
    base = int(base)
    result = math.log(first_num, base)
    print(f"{result :.2f}")

except ValueError:
    if base == "natural":
        result = math.log(first_num)
        print(f"{result:.2f}")
    else:
        print("Invalid input!")
