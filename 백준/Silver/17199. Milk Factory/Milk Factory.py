import sys

N = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[b].append(a)
answer = -1
for n in range(1, N+1):
    visit = [0] * (N+1)
    cnt = 1
    Q = [n]
    visit[n] = 1
    while Q:
        e = Q.pop()
        for node in graph[e]:
            if not visit[node]:
                visit[node] = 1
                cnt += 1
                Q.append(node)
    if cnt == N:
        answer = n
        break
print(answer)