import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [list(map(int, sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
V = set()
info = dict()

for i in range(N):
    for j in range(N):
        e = arr[i][j]
        if e not in V and e:
            V.add(e)
            info[e] = [N, -1, N, -1]
        if e:
            info[e] = [min(info[e][0], i), max(info[e][1], i), min(info[e][2], j), max(info[e][3], j)]

for key in info:
    for i in range(info[key][0], info[key][1] + 1):
        for j in range(info[key][2], info[key][3] + 1):
            e = arr[i][j]
            if e != key and e in V:
                V.remove(e)

print(len(V))