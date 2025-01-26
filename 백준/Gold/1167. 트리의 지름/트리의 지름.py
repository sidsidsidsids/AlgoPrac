import sys

V = int(sys.stdin.readline().strip())
path = [[] for _ in range(V+1)]
for v in range(V):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    arr.pop()
    cur = arr[0]
    for i in range(1, len(arr), 2):
        pos = arr[i]
        val = arr[i+1]
        path[cur].append((pos, val))

maxima = 0
target = -1
Q = [(1, 0)]
visit = [0] * (V+1)
while Q:
    cur, val = Q.pop()
    visit[cur] = 1
    if val > maxima:
        maxima = val
        target = cur
    for node, dist in path[cur]:
        if not visit[node]:
            Q.append((node, val + dist))

Q = [(target, 0)]
visit = [0] * (V+1)
maxima = 0
while Q:
    cur, val = Q.pop()
    visit[cur] = 1
    if val > maxima:
        maxima = val
    for node, dist in path[cur]:
        if not visit[node]:
            Q.append((node, val + dist))

print(maxima)