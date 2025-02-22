import sys

N = int(sys.stdin.readline().strip())
T = []
for _ in range(N):
    T.append(tuple(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline().strip())

answer = 0
hash_maps = [dict() for _ in range(N)]
for n in range(N):
    a, b = T[n]
    for m in range(1, M+1):
        hash_maps[n][a*m + b] = m

for key, val in hash_maps[0].items():
    acc = val
    for n in range(1, N):
        if key in hash_maps[n]:
            acc += hash_maps[n][key]
        else:
            break
    else:
        if acc == M:
            answer = key
            break
print(answer)