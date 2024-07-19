import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
arr = []
for _ in range(M):
    arr.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))

loc = [0] * N
dist = 0
for n in range(N):
    dim = [0] * M
    for m in range(M):
        dim[m] = arr[m][n]
    dim.sort()
    mid = M // 2
    med = dim[mid]

    for m in range(M):
        dist += abs(dim[m] - med)
    loc[n] = med

print(dist)
print(*loc)