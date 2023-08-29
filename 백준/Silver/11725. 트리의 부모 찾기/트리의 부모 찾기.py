from collections import deque

def DFS():
    Q = deque()
    Q.append(1)
    V[1] = 1

    while Q:
        elem = Q.pop()
        for next in nodes[elem]:
            if not V[next]:
                Q.append(next)
                ans[next] = elem
                V[next] = 1

N = int(input())
nodes = [False] + [[] for _ in range(N)]

for n in range(N-1):
    a, b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

V = [0 for _ in range(N+1)]
ans = [0 for _ in range(N+1)]

DFS()
for i in range(2,N+1):
    print(ans[i])


