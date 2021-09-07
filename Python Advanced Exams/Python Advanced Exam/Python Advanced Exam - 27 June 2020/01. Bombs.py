from collections import deque

a = [int(el) for el in input().split(', ')]
bomb_effects = deque(a)
bomb_casings = [int(el) for el in input().split(', ')]

bombs_count = {'datura': 0, 'cherry': 0, 'smoke_decoy': 0}
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# TODO: List as stacks and queeus (popleft etc)
# TODO: 90/100
has_broken = False

for el in range(len(bomb_effects)):
    if has_broken:
        break
    for e in range(len(bomb_casings) - 1, -1, -1):
        if bombs_count['datura'] >= 3 and bombs_count['cherry'] >= 3 and bombs_count['smoke_decoy'] >= 3:
            print('Bene! You have successfully filled the bomb pouch!')
            has_broken = True
            break

        if bomb_effects[0] + bomb_casings[-1] in [40, 60, 120]:
            if bomb_effects[0] + bomb_casings[-1] == 40:
                bombs_count['datura'] += 1
                bomb_effects.popleft()
                bomb_casings.pop()

            elif bomb_effects[0] + bomb_casings[-1] == 60:
                bombs_count['cherry'] += 1
                bomb_effects.popleft()
                bomb_casings.pop()

            else:
                bombs_count['smoke_decoy'] += 1
                bomb_effects.popleft()
                bomb_casings.pop()

        else:
            bomb_casings[-1] -= 5


if not has_broken:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print("Bomb Effects: " + ', '.join([str(el) for el in bomb_effects]))
else:
    print('Bomb Effects: empty')
if bomb_casings:
    print("Bomb Casings: " + ', '.join([str(el) for el in bomb_casings]))
else:
    print('Bomb Casings: empty')

print(f'Cherry Bombs: {bombs_count["cherry"]}')
print(f'Datura Bombs: {bombs_count["datura"]}')
print(f'Smoke Decoy Bombs: {bombs_count["smoke_decoy"]}')