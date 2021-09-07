import re

with open('text.txt', 'w+') as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")

file = open('text.txt')
for index, line in enumerate(file.readlines()):
    if index % 2 != 0:
        continue

    line = re.sub('[-,.!?]', '@', line)
    line = ' '.join(reversed(line.split()))

    print(line.strip())