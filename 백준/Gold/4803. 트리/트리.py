import sys

trial = 1

def cycle(x):
    Q = [x]
    flag = False
    while Q:
        elem = Q.pop()
        if V[elem]:
            flag = True
        V[elem] = 1
        for n in graph[elem]:
            if not V[n]:
                Q.append(n)
    return flag

while True:
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    if not N and not M:
        break

    graph = [[] for _ in range(N+1)]

    for m in range(M):
        s, e = map(int, sys.stdin.readline().rstrip('\n').split())
        graph[s].append(e)
        graph[e].append(s)

    V = [0] * (N+1)
    tree = 0
    for i in range(1, N+1):
        if not V[i]:
            if not cycle(i):
                tree += 1

    if not tree:
        print(f'Case {trial}: No trees.')
    elif tree == 1:
        print(f'Case {trial}: There is one tree.')
    else:
        print(f'Case {trial}: A forest of {tree} trees.')

    trial += 1