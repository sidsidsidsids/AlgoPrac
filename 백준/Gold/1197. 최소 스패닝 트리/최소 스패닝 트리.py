import heapq
import sys

V, E = map(int,sys.stdin.readline().rstrip("\n").split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, v = map(int,sys.stdin.readline().rstrip("\n").split())
    graph[s].append((e, v))
    graph[e].append((s, v))

hq = [(0, 1)]
visit = [0] * (V+1)
answer = 0
while hq:
    weight, pos = heapq.heappop(hq)
    if not visit[pos]:
        visit[pos] = 1
        answer += weight
        for node, cost in graph[pos]:
            if not visit[node]:
                heapq.heappush(hq, (cost, node))

print(answer)