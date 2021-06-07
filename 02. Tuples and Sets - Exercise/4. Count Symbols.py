# # dictionary solution
#
# text = input()
# occurances_dict = dict()
#
# for el in text:
#     if el not in occurances_dict:
#         occurances_dict[el] = 1
#     else:
#         occurances_dict[el] += 1
#
# for key, value in sorted(occurances_dict.items()):
#     print(f"{key}: {value} time/s")
#
# # tuple solution

text = input()
occurances_tuple = []
for each_letter in text:
    occurances_tuple.append(each_letter)

occurances_tuple = tuple(occurances_tuple)

for letter in sorted(set(occurances_tuple)):
    print(f'{letter}: {occurances_tuple.count(letter)} time/s')