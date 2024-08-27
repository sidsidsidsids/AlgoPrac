import sys
import heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().rstrip('\n').split())
K = int(sys.stdin.readline().rstrip('\n'))

graph = defaultdict(list)
dist = defaultdict(dict)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip('\n').split())
    graph[u].append(v)
    if v in dist[u]:
        dist[u][v] = min(dist[u][v], w)
    else:
        dist[u][v] = w

INF = sys.maxsize
record = [INF] * (V+1)
pq = []
pq.append((0, K))

while pq:
    d, l = heapq.heappop(pq)
    if record[l] <= d:
        continue

    record[l] = d
    for nl in graph[l]:
        heapq.heappush(pq, (dist[l][nl] + d, nl))

for i in range(1, V + 1):
    print(record[i] if record[i] != INF else "INF")