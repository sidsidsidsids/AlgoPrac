import sys

N, M, K = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
C = [0] + list(map(int, sys.stdin.readline().strip().split()))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
V = [0] * (N+1)
lst = []
lst_len = 0
for i in range(1, N+1):
    if V[i]:
        continue
    V[i] = 1
    Q = [i]
    candy = 0
    cry = 0
    lst_len += 1
    while Q:
        elem = Q.pop()
        cry += 1
        candy += C[elem]
        for node in graph[elem]:
            if not V[node]:
                V[node] = 1
                Q.append(node)
    lst.append((candy, cry))

dp = [0] * K
for candy, cry in lst:
    for k in range(K-1, 0, -1):
        if k - cry < 0:
            break
        dp[k] = max(dp[k], dp[k-cry] + candy)
print(dp[-1])