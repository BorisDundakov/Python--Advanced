# text = input()
# result = ""
# for el in text:
#     if el == "a":
#         pass
#     elif el == "i":
#         pass
#     elif el == "o":
#         pass
#     elif el == "u":
#         pass
#     else:
#         result += el
#
# print(result)

vowels = ['a', 'e', 'i', 'o', 'u']
text = input()
result = []
result += [el for el in text if el.lower() not in vowels]
print(''.join(result))
