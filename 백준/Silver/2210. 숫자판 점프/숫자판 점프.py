grid = [list(input().split()) for _ in range(5)]
hashSet = set()
dy = (1, 0, -1 ,0)
dx = (0, 1, 0, -1)
for i in range(5):
    for j in range(5):
        Q = [(i, j, grid[i][j], 0)]
        while Q:
            y, x, s, cnt = Q.pop()
            if cnt == 5:
                if s not in hashSet:
                    hashSet.add(s)
                continue
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny <= 4 and 0 <= nx <= 4:
                    Q.append((ny, nx, s + grid[ny][nx], cnt + 1))
print(len(hashSet))