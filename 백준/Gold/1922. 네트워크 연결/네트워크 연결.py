import sys
from collections import defaultdict
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
M = int(sys.stdin.readline().rstrip('\n'))
graph = defaultdict(dict)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
    graph[a][b] = c
    graph[b][a] = c

V = [0] * (N+1)
Q = [(0, 1)]
answer = 0
while Q:
    cost, pos = heapq.heappop(Q)
    if not V[pos]:
        V[pos] = 1
        answer += cost
        for key, val in graph[pos].items():
            if not V[key]:
                heapq.heappush(Q, (val, key))

print(answer)