bomb_effects = [int(el) for el in input().split(', ')]
bomb_casings = [int(el) for el in input().split(', ')]

bombs_count = {'datura': 0, 'cherry': 0, 'smoke_decoy': 0}
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120\
# TODO: List as stacks and queeus (popleft etc)
# TODO: 20/100


for el in range(len(bomb_effects)):
    for e in range(len(bomb_casings)-1, -1, -1):
        print(bomb_casings[e])