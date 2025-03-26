import sys

M, N = map(int, sys.stdin.readline().strip().split())
D = [0] * 1000001
for n in range(2, 1000001):
    if not D[n]:
        if M <= n <= N:
            print(n)
        for nn in range(n+n, 1000001, n):
            D[nn] = 1