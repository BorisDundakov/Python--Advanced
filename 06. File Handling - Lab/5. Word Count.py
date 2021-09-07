import re

with open('words.txt') as words_fh, open('input.txt') as input_fh:
    words = words_fh.read().split()
    text = input_fh.read()

word_occurences = {}

for word in words:
    matches = re.findall(rf'[\s-]({word})[\s.,?!]', text, re.MULTILINE + re.IGNORECASE)
    word_occurences[word.lower()] = len(matches)

for word, occurence in sorted(word_occurences.items(), key=lambda t: -t[1]):
    print(f'{word} - {occurence}')
