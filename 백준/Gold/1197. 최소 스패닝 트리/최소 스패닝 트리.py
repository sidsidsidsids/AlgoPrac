import heapq
import sys

V, E = map(int,sys.stdin.readline().rstrip("\n").split())
graph = dict()
for _ in range(E):
    s, e, v = map(int,sys.stdin.readline().rstrip("\n").split())
    if s not in graph:
        graph[s] = dict()
    if e not in graph:
        graph[e] = dict()
    graph[s][e] = v
    graph[e][s] = v

hq = [(0, 1)]
V = [0] * (V+1)
answer = 0
while hq:
    weight, pos = heapq.heappop(hq)
    if not V[pos]:
        V[pos] = 1
        answer += weight
        for key, val in graph[pos].items():
            if not V[key]:
                heapq.heappush(hq, (val, key))

print(answer)
