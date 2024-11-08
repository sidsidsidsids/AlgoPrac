import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
path = defaultdict(list)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    path[A].append(B)
    path[B].append(A)

V = [0] * N
flag = False
def dfs(cur, dep):
    global flag
    if flag:
        return
    if dep >= 4:
        flag = True
        return
    for nxt in path[cur]:
        if not V[nxt]:
            V[nxt] = 1
            dfs(nxt, dep + 1)
            V[nxt] = 0
for key in path.keys():
    V[key] = 1
    dfs(key, 0)
    V[key] = 0
    if flag:
        break

print(1 if flag else 0)