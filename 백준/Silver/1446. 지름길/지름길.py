N, D = map(int,input().split())
path = [i for i in range(D+1)]
shortcut = [[] for _ in range(N)]

for n in range(N):
    s, e, d = map(int,input().split())
    shortcut[n] = [s, e, d]
shortcut = sorted(shortcut, key = lambda X:(X[1], X[0]))

for way in shortcut:
    s, e, d = way[0], way[1], way[2]
    if d > e-s or e > D:
        continue
    tmp = path[e]
    path[e] = min(path[s] + d, path[e])
    if path[e] == tmp:
        pass
    else:
        for idx in range(e+1, D+1):
            path[idx] = min(path[idx-1] + 1, path[idx])
print(path[D])