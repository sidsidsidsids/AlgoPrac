import sys
from collections import deque

dy = (-2, -1, 1, 2, 2, 1, -1, -2)
dx = (1, 2, 2, 1, -1, -2, -2, -1)

while True:
    try:
        R, C, Gr, Gc, Lr, Lc = map(int, sys.stdin.readline().rstrip('\n').split())
        V = [[0] * (C+1) for _ in range(R+1)]
        Q = deque()
        Q.append((Gr, Gc))
        V[Gr][Gc] = 1
        L = 1
        step = 0
        flag = False
        while Q:
            y, x = Q.popleft()
            L -= 1
            if y == Lr and x == Lc:
                flag = True
                break
            for d in range(8):
                ny = y + dy[d]
                nx = x + dx[d]
                if 1 <= ny <= R and 1 <= nx <= C and not V[ny][nx]:
                    Q.append((ny, nx))
                    V[ny][nx] = 1
            if L == 0:
                L = len(Q)
                step += 1
        print(step if flag else "impossible")
    except Exception:
        break