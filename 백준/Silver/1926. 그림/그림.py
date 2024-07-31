import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

V = [[0] * M for _ in range(N)]
cnt = 0
sq = 0
for n in range(N):
    for m in range(M):
        if arr[n][m] and not V[n][m]:
            Q = deque()
            Q.append((n, m))
            V[n][m] = 1
            tmp = 1
            cnt += 1
            while Q:
                y, x = Q.popleft()
                for ny, nx in ((y-1, x), (y, x+1), (y+1, x), (y,x-1)):
                    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] and not V[ny][nx]:
                        V[ny][nx] = 1
                        tmp += 1
                        Q.append((ny, nx))
            sq = max(sq, tmp)
print(cnt)
print(sq)

