N, Q = map(int,input().split())
dist = [[0] * (N+1) for _ in range(N+1)]
path = [[] for _ in range(N+1)]

for n in range(N-1):
    a, b, r = map(int,input().split())
    dist[a][b] = r
    dist[b][a] = r
    path[a].append(b)
    path[b].append(a)

checked = dict()
maxima = 100000001

for _ in range(Q):
    k, v = map(int,input().split())
    if v in checked:
        pass
    else:
        value = [maxima] * (N+1)
        visit = [0] * (N+1)
        stack = [v]
        visit[v] = 1

        while stack:
            elem = stack.pop()
            for nelem in path[elem]:
                if not visit[nelem]:
                    stack.append(nelem)
                    value[nelem] = min(value[elem],dist[elem][nelem])
                    visit[nelem] = 1

        checked[v] = value
    ans = 0
    for val in checked[v]:
        if val != maxima and val >= k:
            ans += 1
    print(ans)


