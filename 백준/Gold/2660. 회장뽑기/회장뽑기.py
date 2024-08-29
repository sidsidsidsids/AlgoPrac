import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))
graph = [[] for _ in range(N+1)]

while True:
    a, b = map(int, sys.stdin.readline().rstrip('\n').split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

INF = sys.maxsize
minima = INF
cand = []

for n in range(1, N+1):
    d = deque()
    d.append(n)
    v = [0] * (N+1)
    v[n] = 1
    cnt = 0
    L = 1

    while d:
        e = d.popleft()
        L -= 1
        for ne in graph[e]:
            if not v[ne]:
                v[ne] = 1
                d.append(ne)
        if L == 0:
            L = len(d)
            if L:
                cnt += 1

    if cnt and cnt <= minima:
        if cnt == minima:
            cand.append(n)
        else:
            minima = cnt
            cand = [n]

print(minima, len(cand))
print(*cand)