from collections import deque
N, M = map(int,input().split())
array = [list(input()) for _ in range(N)]

def func(Y, X, arr):
    answer = 0
    def bfs(sy, sx):
        Q = deque()
        Q.append([sy, sx])
        V = [[0] * M for _ in range(N)]
        V[sy][sx] = 1
        len_Q = 1
        cnt = 0
        while Q:
            elem = Q.popleft()
            len_Q -= 1
            cy, cx = elem[0], elem[1]
            for ny, nx in [[cy + 1, cx], [cy, cx + 1], [cy - 1, cx], [cy, cx - 1]]:
                if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 'L' and not V[ny][nx]:
                    Q.append([ny, nx])
                    V[ny][nx] = 1
            if not len_Q and Q:
                len_Q = len(Q)
                cnt += 1
        return cnt
    for y in range(Y):
        for x in range(X):
            if arr[y][x] == 'L':
                val = bfs(y, x)
                if answer < val:
                    answer = val
    return answer

print(func(N, M, array))
