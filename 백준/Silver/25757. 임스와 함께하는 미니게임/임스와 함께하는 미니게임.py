import sys

N, G = sys.stdin.readline().rstrip('\n').split()

M = int
if G == 'Y':
    M = 2
elif G == 'F':
    M = 3
elif G == 'O':
    M = 4

ls = set()
room = 1
play = 0
for _ in range(int(N)):
    user = sys.stdin.readline().rstrip('\n')
    if user in ls:
        pass
    else:
        ls.add(user)
        room += 1
        if room == M:
            play += 1
            room = 1

print(play)