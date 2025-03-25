import sys
from collections import deque

N = int(sys.stdin.readline().strip())
Q = deque()
for _ in range(N):
    io = list(sys.stdin.readline().strip().split())
    t = io[0]
    if t == "push":
        Q.append(int(io[1]))
    elif t == "pop":
        print(-1 if not Q else Q.popleft())
    elif t == "size":
        print(len(Q))
    elif t == "empty":
        print(0 if Q else 1)
    elif t == "front":
        print(Q[0] if Q else -1)
    elif t == "back":
        print(Q[-1] if Q else -1)