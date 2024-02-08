import heapq
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = dict()
for _ in range(M):
    a, b, c = map(int,input().split())
    if a in graph:
        if b in graph[a]:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    else:
        graph[a] = dict()
        graph[a][b] = c
    if b in graph:
        if a in graph[b]:
            graph[b][a] = min(graph[b][a], c)
        else:
            graph[b][a] = c
    else:
        graph[b] = dict()
        graph[b][a] = c
V = [0] * (N+1)
arr = [1000 * N + 1] * (N+1)
V[1] = 1; arr[1] = 0
Q = list()
heapq.heappush(Q, [arr[1], 1])

while Q:
    cur_cost, cur_pos = heapq.heappop(Q)
    if arr[cur_pos] < cur_cost:
        continue
    for next_pos, next_cost in graph[cur_pos].items():
        new_cost = cur_cost + next_cost
        if new_cost < arr[next_pos]:
            arr[next_pos] = new_cost
            heapq.heappush(Q, [new_cost, next_pos])

print(arr[N])

