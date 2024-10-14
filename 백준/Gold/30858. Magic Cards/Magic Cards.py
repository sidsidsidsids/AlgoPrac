import sys

N, K, M, F = map(int, sys.stdin.readline().rstrip('\n').split())
cards = []
for _ in range(K):
    cards.append(set(map(int, sys.stdin.readline().rstrip('\n').split())))

info = dict()
for n in range(1, N+1):
    result = ""
    for card in cards:
        if n in card:
            result += "Y"
        else:
            result += "N"
    if result in info:
        info[result] = -1
    else:
        info[result] = n

for _ in range(F):
    answer = sys.stdin.readline().rstrip('\n')
    if answer in info and info[answer] != -1:
        print(info[answer])
    else:
        print(0)