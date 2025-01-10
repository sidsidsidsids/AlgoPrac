import sys
sys.setrecursionlimit(100001)
N, S, E = map(int, sys.stdin.readline().strip().split())
path = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().strip().split())
    path[u].append(v)
    path[v].append(u)

flag = False
Q = [S]
visit[S] = 1
def func(idx):
    global flag
    if idx == E:
        flag = True
    if flag:
        return
    for node in path[idx]:
        if not visit[node]:
            Q.append(node)
            visit[node] = 1
            func(node)
            if flag:
                return
            Q.pop()
            visit[node] = 0
    return
func(S)

if flag:
    if len(Q) <= 2:
        print("First")
    else:
        for i in range(1, len(Q)-1, 2):
            if len(path[Q[i]]) > 2:
                print("Second")
                break
        else:
            print("First")
else:
    print("Second")