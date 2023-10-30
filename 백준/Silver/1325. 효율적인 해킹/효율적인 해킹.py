import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

nodes = [[] for _ in range(N+1)]

for m in range(M):
    e, s = map(int,sys.stdin.readline().split())
    nodes[s].append(e)

maximum = 1
result = []
for n in range(1, N+1):
    cnt = 1
    if nodes[n]:
        Q = deque()
        Q.append(n)
        V = [0] * (N+1)
        V[n] = 1
        while Q:
            elem = Q.popleft()
            for next in nodes[elem]:
                if not V[next]:
                    Q.append(next)
                    V[next] = 1
                    cnt += 1
    if cnt > maximum:
        result = [n]
        maximum = cnt
    elif cnt == maximum:
        result.append(n)
print(*sorted(result))