import sys
from collections import defaultdict
T = int(sys.stdin.readline().strip())
answer = [0] * T
for t in range(T):
    info = defaultdict(list)
    hs = set()
    docs = 0
    Q = []
    H, W = map(int, sys.stdin.readline().strip().split())
    visit = [[0] * W for _ in range(H)]
    grid = [list(sys.stdin.readline().strip()) for _ in range(H)]
    keys = sys.stdin.readline().strip()
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '.' and (h == 0 or h == H-1 or w == 0 or w == W-1):
                Q.append((h, w))
                visit[h][w] = 1
            elif grid[h][w] == '$' and (h == 0 or h == H-1 or w == 0 or w == W-1):
                docs += 1
                grid[h][w] = '.'
                Q.append((h, w))
                visit[h][w] = 1
            elif grid[h][w].islower() and (h == 0 or h == H-1 or w == 0 or w == W-1):
                if keys == '0':
                    keys = grid[h][w]
                else:
                    keys += grid[h][w]
                grid[h][w] = '.'
                Q.append((h, w))
                visit[h][w] = 1
            elif grid[h][w].isupper():
                info[grid[h][w]].append((h, w))
                hs.add(grid[h][w])
    if keys != '0':
        for elem in keys:
            if elem.upper() in info:
                for y, x in info[elem.upper()]:
                    grid[y][x] = '.'
                    if y == 0 or y == H-1 or x == 0 or x == W-1:
                        Q.append((y, x))
                        visit[y][x] = 1
    while Q:
        y, x = Q.pop()
        for ny, nx in [(y-1, x),(y, x+1),(y+1, x),(y, x-1)]:
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '*' and not visit[ny][nx]:
                if grid[ny][nx] == '.':
                    visit[ny][nx] = 1
                    Q.append((ny, nx))
                elif grid[ny][nx].islower():
                    visit[ny][nx] = 1
                    Q.append((ny, nx))
                    if grid[ny][nx].upper() in hs:
                        hs.remove(grid[ny][nx].upper())
                        for i, j in info[grid[ny][nx].upper()]:
                            grid[i][j] = '.'
                            for ni, nj in [(i-1, j),(i, j+1),(i+1, j),(i, j-1)]:
                                if (0 <= ni < H and 0 <= nj < W and visit[ni][nj]) or \
                                        (ni == 0 or ni == H-1 or nj == 0 or nj == W-1):
                                    Q.append((i, j))
                                    visit[i][j] = 1
                                    break
                    grid[ny][nx] = '.'
                elif grid[ny][nx] == '$':
                    docs += 1
                    grid[ny][nx] = '.'
                    Q.append((ny, nx))
                    visit[ny][nx] = 1
    answer[t] = docs
print("\n".join(map(str, answer)))