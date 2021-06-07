a = input()
final_list = []
answer_list = []
f_counter = 3
c_counter = 0
defuser = False
for each_letter in a:
    if c_counter < f_counter:
        final_list.extend(each_letter)
        c_counter += 1
    else:
        answer_list.extend(final_list)
        final_list = []
        final_list.extend(each_letter)
        c_counter = 0
        continue

print(final_list)
print(answer_list)
