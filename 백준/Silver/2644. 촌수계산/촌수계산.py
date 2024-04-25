import sys
from collections import deque
N = int(sys.stdin.readline().rstrip("\n"))
graph = dict()
visit = [-1] * (N+1)
s, e = map(int,sys.stdin.readline().rstrip("\n").split())
M = int(sys.stdin.readline().rstrip("\n"))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip("\n").split())
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

Q = deque()
Q.append(s)
flag = False
visit[s] = 0
while Q:
    elem = Q.popleft()
    for next_elem in graph[elem]:
        if visit[next_elem] == -1:
            Q.append(next_elem)
            visit[next_elem] = visit[elem] + 1
        if next_elem == e:
            flag = True
            break
    if flag:
        break
print(visit[e])

