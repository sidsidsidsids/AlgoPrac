from collections import deque
import sys

sys.setrecursionlimit(10**6)
N, M, R = map(int,sys.stdin.readline().split())
path = [[] * (N+1) for _ in range(N+1)]
for m in range(M):
    u, v = map(int,sys.stdin.readline().split())
    path[u].append(v)
    path[v].append(u)

visit = [0] * (N+1)
order = [0] * (N+1)
Q = deque()
Q.append(R)
visit[R] = 1
order[R] = 1
cnt = 1
def dfs(start):
    global cnt
    for next in sorted(path[start]):
        if not visit[next]:
            visit[next] = 1
            cnt += 1
            order[next] = cnt
            dfs(next)
    else:
        return
dfs(R)
for n in range(1,N+1):
    print(order[n])