line = input().split()
even_words_len = []
[even_words_len.append(word) for word in line if len(word) % 2 == 0]
print('\n'.join(even_words_len))