import sys

N, S, P = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
crit = set(s for s in range(1, S+1))
for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().strip().split())
    graph[B].append(A)
    graph[A].append(B)
visit = [0] * (N+1)
Q = [(P, 0)]
visit[P] = 1
dists = []
while Q:
    e, d = Q.pop()
    if e in crit:
        dists.append(d)
        continue
    for node in graph[e]:
        if not visit[node]:
            visit[node] = 1
            Q.append((node, d+1))
dists = sorted(dists)
print(N - (dists[0] + dists[1] + 1))