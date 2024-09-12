import sys

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    n, x = sys.stdin.readline().rstrip('\n').split()
    print(x * int(n))
