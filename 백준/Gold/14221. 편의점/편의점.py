import sys
from collections import defaultdict
import heapq

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
graph = defaultdict(dict)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
    graph[a][b] = c
    graph[b][a] = c
P, Q = map(int, sys.stdin.readline().rstrip('\n').split())
homes = sorted(list(map(int, sys.stdin.readline().rstrip('\n').split())))
targets = set(map(int, sys.stdin.readline().rstrip('\n').split()))

INF = sys.maxsize
dist = [INF] * (N+1)
Q = []
for target in targets:
    heapq.heappush(Q, (0, target))
    dist[target] = 0
while Q:
    d, v = heapq.heappop(Q)
    if dist[v] < d:
        continue
    for n_v, n_d in graph[v].items():
        new_dist = d + n_d
        if new_dist < dist[n_v]:
            dist[n_v] = new_dist
            heapq.heappush(Q, (new_dist, n_v))

answer = 0
closest = INF
for home in homes:
    if dist[home] < closest:
        answer = home
        closest = dist[home]

print(answer)