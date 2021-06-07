n_usernames = int(input())
usernames_set = set()
[usernames_set.add(input()) for el in range(n_usernames)]
print([el for el in usernames_set])
