import sys

N = int(sys.stdin.readline().strip())
for _ in range(N):
    r, e, c = map(int, sys.stdin.readline().strip().split())
    if r == e - c:
        print("does not matter")
    elif r < e - c:
        print("advertise")
    elif r > e - c:
        print("do not advertise")