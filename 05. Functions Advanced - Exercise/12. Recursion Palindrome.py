
def palindrome(word):
    first_index = word[0]
    last_index = word[-1]
    wordlist = []

    for letter in word:
        wordlist.append(letter)

    if len(wordlist) > 1:
        if first_index == last_index:
            wordlist.remove(wordlist[0])
            wordlist.remove(wordlist[-1])
            return palindrome(wordlist)
        else:
            return f'{"".join(word)} is not a palindrome'
    return f'{"".join(word)} is a palindrome'

print(palindrome("abcba"))
print(palindrome("peter"))