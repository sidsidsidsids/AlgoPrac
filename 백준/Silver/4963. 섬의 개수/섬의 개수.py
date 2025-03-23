import sys

dy = (-1, 0, 1, 0, -1, -1, 1, 1)
dx = (0, 1, 0, -1, -1, 1, -1, 1)
while True:
    W, H = map(int, sys.stdin.readline().strip().split())
    if not W and not H:
        break
    grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H)]
    visit = [[0] * W for _ in range(H)]
    counter = 1
    for h in range(H):
        for w in range(W):
            if grid[h][w] and not visit[h][w]:
                Q = [(h, w)]
                visit[h][w] = counter
                while Q:
                    y, x = Q.pop()
                    for d in range(8):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] and not visit[ny][nx]:
                            Q.append((ny, nx))
                            visit[ny][nx] = counter
                counter += 1
    print(counter - 1)