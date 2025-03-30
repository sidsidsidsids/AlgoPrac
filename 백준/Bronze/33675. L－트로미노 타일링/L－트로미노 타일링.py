import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    if N % 2:
        print(0)
    else:
        print(2 ** (N // 2))