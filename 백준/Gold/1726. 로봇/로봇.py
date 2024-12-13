import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
factory = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
visit = [0] + [[[0] * M for _ in range(N)] for _ in range(4)]

s_i, s_j, s_d = map(int, sys.stdin.readline().rstrip('\n').split())
s_i -= 1
s_j -= 1
e_i, e_j, e_d = map(int, sys.stdin.readline().rstrip('\n').split())
e_i -= 1
e_j -= 1

def turn_path(y, x, d):
    if d == 1 or d == 2:
        return [(y, x, 3), (y, x, 4)]
    elif d == 3 or d == 4:
        return [(y, x, 1), (y, x, 2)]

def go_path(y, x, d):
    nodes = []
    if d == 1:
        for k in range(1, 4):
            if x+k < M and factory[y][x+k] == 0:
                nodes.append((y, x+k, 1))
            else:
                break
    elif d == 2:
        for k in range(1, 4):
            if -1 < x-k and factory[y][x-k] == 0:
                nodes.append((y, x-k, 2))
            else:
                break
    elif d == 3:
        for k in range(1, 4):
            if y+k < N and factory[y+k][x] == 0:
                nodes.append((y+k, x, 3))
            else:
                break
    elif d == 4:
        for k in range(1, 4):
            if -1 < y-k and factory[y-k][x] == 0:
                nodes.append((y-k, x, 4))
            else:
                break
    return nodes

Q = deque()
Q.append((s_i, s_j, s_d))
visit[s_d][s_i][s_j] = 1
turn = 0
Q_size = 1
while Q:
    y, x, d = Q.popleft()
    Q_size -= 1
    if y == e_i and x == e_j and d == e_d:
        break
    nodes = turn_path(y, x, d)
    for node in nodes:
        ny, nx, nd = node
        if 0 <= ny < N and 0 <= nx < M and factory[ny][nx] == 0 and not visit[nd][ny][nx]:
            visit[nd][ny][nx] = 1
            Q.append((ny, nx, nd))
    nodes = go_path(y, x, d)
    for node in nodes:
        ny, nx, nd = node
        if 0 <= ny < N and 0 <= nx < M and not visit[nd][ny][nx]:
            visit[nd][ny][nx] = 1
            Q.append((ny, nx, nd))
    if Q_size == 0:
        turn += 1
        Q_size = len(Q)
print(turn)