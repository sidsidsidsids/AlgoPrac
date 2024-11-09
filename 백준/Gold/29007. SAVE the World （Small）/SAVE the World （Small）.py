import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))
info = dict()
arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split())
    info[(x, y)] = ''
    arr.append((x, y))

cx = 0
cy = 0
depth = 1
S = deque()

def check(x, y):
    if (x, y) in info:
        s = ''
        for e in S:
            s += e
        info[(x, y)] = s
    return
while depth <= 32:
    for _ in range(depth):
        cx += 1
        S.appendleft('A')
        check(cx, cy)
    for _ in range(depth):
        cy -= 1
        S.appendleft('W')
        check(cx, cy)
    depth += 1
    for _ in range(depth):
        cx -= 1
        S.appendleft('D')
        check(cx, cy)
    for _ in range(depth):
        cy += 1
        S.appendleft('X')
        check(cx, cy)
    depth += 1

for elem in arr:
    print(info[elem])