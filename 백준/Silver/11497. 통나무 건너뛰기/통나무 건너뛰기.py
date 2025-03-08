import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    L = list(map(int, sys.stdin.readline().strip().split()))
    sL = sorted(L, reverse=True)
    D = deque()
    diff = 0
    for n in range(N):
        if n%2:
            D.append(sL[n])
            diff = max(diff, D[-2]-D[-1])
        else:
            D.appendleft(sL[n])
            if n:
                diff = max(diff, D[1]-D[0])
    print(diff)