import sys

a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
W = sys.stdin.readline().rstrip('\n')
P = sys.stdin.readline().rstrip('\n')

info = dict()
cost = dict()
for word in W:
    info[word] = -1
    cost[word] = 0

L = len(P)
for i in range(L):
    word = P[i]
    if info[word] == -1:
        info[word] = i
        cost[word] += c
        cost[word] += b
        continue
    dist = i - info[word] - 1
    cost[word] += min(a * dist, c * 2)
    info[word] = i
    cost[word] += b

for word in W:
    if info[word] != -1:
        cost[word] += c
    print(cost[word])