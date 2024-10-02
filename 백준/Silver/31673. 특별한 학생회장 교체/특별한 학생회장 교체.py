import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
V = list(map(int, sys.stdin.readline().rstrip('\n').split()))

T = sum(V)
half = T // 2
if T % 2:
    half += 1
V = sorted(V, reverse=True)

C = 1
voted = 0
for m in range(M):
    C += 1
    voted += V[m]
    if voted >= half:
        break

print(M // C)