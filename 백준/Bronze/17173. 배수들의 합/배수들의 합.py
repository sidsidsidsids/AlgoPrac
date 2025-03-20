import sys

N, M = map(int, sys.stdin.readline().strip().split())
V = [0] * 1001
K = list(map(int, sys.stdin.readline().strip().split()))
A = 0
for k in K:
    for i in range(k, N+1, k):
        if not V[i]:
            A += i
            V[i] = 1
print(A)