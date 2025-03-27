import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    K = [0] * 4
    C = int(sys.stdin.readline().strip())
    for i, c in ((0, 25), (1, 10), (2, 5), (3, 1)):
        K[i] = C // c
        if K[i]:
            C %= K[i] * c
    print(*K)