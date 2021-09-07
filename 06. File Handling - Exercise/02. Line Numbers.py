with open('text.txt') as file:
    line = [line.strip() for line in file.readlines()]

output_list = []
for index, line in enumerate(line):
    punctuations = sum([1 for word in line.split() for letter in word if letter in r'-,\.!?\''])
    letters_count = (sum([len(word) for word in line.split()]) - (
        sum([1 for word in line.split() for letter in word if letter in r'-,\.!?\''])))
    # print(f'({letters_count})({punctuations})')

    output_list.append(f'Line {index + 1}: {line} ({letters_count})({punctuations})')

with open('text.txt', 'w') as output_file:
    output_file.writelines([line + "\n" for line in output_list])
