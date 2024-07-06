import sys
from collections import deque

X, Y, N = map(int, sys.stdin.readline().rstrip('\n').split())
pool = set()
for _ in range(N):
    pool.add(tuple(map(int, sys.stdin.readline().rstrip('\n').split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = set()
Q = deque()
Q.append((0, 0))
visit.add((0, 0))
tmp = 1
dist = 0
while Q:
    x, y = Q.popleft()
    tmp -= 1
    if x == X and y == Y:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if -500 <= nx <= 500 and -500 <= ny <= 500 and (nx, ny) not in pool and (nx, ny) not in visit:
            visit.add((nx, ny))
            Q.append((nx, ny))
    if not tmp:
        tmp = len(Q)
        dist += 1

print(dist)