grid = [list(input()) for _ in range(12)]

answer = 0

while True:
    V = [[0] * 6 for _ in range(12)]
    flag = False

    for y in range(12):
        for x in range(6):
            if grid[y][x] != '.':
                s = [(y, x)]
                t = set()
                t.add((y, x))
                while s:
                    cy, cx = s.pop()
                    for ny, nx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if 0 <= cy + ny < 12 and 0 <= cx + nx < 6 and grid[cy+ny][cx+nx] == grid[y][x] and not V[cy+ny][cx+nx]:
                            V[cy+ny][cx+nx] = 1
                            s.append((cy + ny, cx + nx))
                            t.add((cy+ny, cx+nx))
                if len(t) >= 4:
                    flag = True
                    for puyo in t:
                        V[puyo[0]][puyo[1]] = -1

    if not flag:
        break

    for y in range(12):
        for x in range(6):
            if V[y][x] == -1:
                grid[y][x] = '.'

    for y in range(11, -1, -1):
        for x in range(6):
            if y < 11 and grid[y][x] != '.' and grid[y+1][x] == '.':
                k = 1
                while y+k < 11 and grid[y+k+1][x] == '.':
                    k += 1
                grid[y+k][x] = grid[y][x]
                grid[y][x] = '.'

    answer += 1

print(answer)