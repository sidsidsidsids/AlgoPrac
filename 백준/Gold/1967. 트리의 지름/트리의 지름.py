import sys

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, v = map(int, sys.stdin.readline().strip().split())
    tree[a].append((b, v))
    tree[b].append((a, v))
maxima = -1
target = -1
Q = [(1, 0)]
visit = [0] * (N+1)
visit[1] = 1
while Q:
    cur_pos, cur_dist = Q.pop()
    if cur_dist >= maxima:
        maxima, target = cur_dist, cur_pos
    for node, dist in tree[cur_pos]:
        if not visit[node]:
            Q.append((node, cur_dist + dist))
            visit[node] = 1
Q = [(target, 0)]
visit = [0] * (N+1)
visit[target] = 1
maxima = -1
target = -1
while Q:
    cur_pos, cur_dist = Q.pop()
    if cur_dist >= maxima:
        maxima, target = cur_dist, cur_pos
    for node, dist in tree[cur_pos]:
        if not visit[node]:
            Q.append((node, cur_dist + dist))
            visit[node] = 1
print(maxima)