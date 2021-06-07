number_of_students = int(input())
student_kvp = {}
for student in range(number_of_students):
    command = input().split()
    if command[0] not in student_kvp:
        student_kvp[command[0]] = [float(command[1])]
    else:
        student_kvp[command[0]].append(float(command[1]))

for key, value in sorted(student_kvp.items()):
    print(f'{key} -> {" ".join(map(str, value))} (avg: {sum(value) / len(value):.2f})')
