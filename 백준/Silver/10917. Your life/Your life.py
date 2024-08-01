import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip('\n').split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split())
    graph[x].append(y)

V = [0] * (N+1)
Q = deque()
Q.append(1)
flag = False
step = 1
stage = 1
while Q:
    elem = Q.popleft()
    for next_elem in graph[elem]:
        if not V[next_elem]:
            if next_elem == N:
                flag = True
                break
            V[next_elem] = 1
            Q.append(next_elem)
    if flag:
        break
    stage -= 1
    if not stage:
        stage = len(Q)
        step += 1

print(step if flag else -1)