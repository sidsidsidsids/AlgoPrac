import sys
import heapq

N, M, T = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, P = map(int, sys.stdin.readline().strip().split())
    graph[B].append((A, P))
    graph[A].append((B, P))
visit = [0] * (N+1)
HQ = [(0, 1)]
answer = 0
while HQ:
    dist, pos = heapq.heappop(HQ)
    if not visit[pos]:
        visit[pos] = 1
        answer += dist
        for node, cost in graph[pos]:
            if not visit[node]:
                heapq.heappush(HQ, (cost, node))
inc_price = 0
for n in range(1, N-1):
    inc_price += n
print(answer + (inc_price * T))