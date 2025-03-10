import sys
from collections import deque

N = int(sys.stdin.readline().strip())
D = deque()
for _ in range(N):
    o = sys.stdin.readline().strip().split()
    t = o[0]
    if t == "push_front":
        D.append(int(o[1]))
    elif t == "push_back":
        D.appendleft(int(o[1]))
    elif t == "pop_front":
        print(D.pop() if D else -1)
    elif t == "pop_back":
        print(D.popleft() if D else -1)
    elif t == "size":
        print(len(D))
    elif t == "empty":
        print(0 if D else 1)
    elif t == "front":
        print(D[-1] if D else -1)
    elif t == "back":
        print(D[0] if D else -1)