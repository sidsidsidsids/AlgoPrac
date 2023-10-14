R, C, M = map(int,input().split())
grid = [[[] for _ in range(C)] for _ in range(R)]

for m in range(M):
    r, c, s, d, z = map(int,input().split())
    grid[r-1][c-1] = [s, d, z]
man = 0
cnt = 0

while man < C:
    temp = [[[] for _ in range(C)] for _ in range(R)]
    # 이동(낚시)
    for y in range(R):
        if grid[y][man]:
            cnt += grid[y][man][2]
            grid[y][man] = []
            break
    # 이동(상어)
    for y in range(R):
        for x in range(C):
            if grid[y][x]:
                if grid[y][x][1] == 1: #위
                    ny = y
                    speed = grid[y][x][0]
                    modified = speed % ((R-1)*2)
                    direct = -1
                    while modified:
                        if 0 <= ny + direct < R:
                            ny += direct
                        else:
                            direct = -direct
                            ny += direct
                        modified -= 1
                    if direct == 1:
                        grid[y][x][1] = 2
                    temp[ny][x].append(grid[y][x])
                elif grid[y][x][1] == 2: #아래
                    ny = y
                    speed = grid[y][x][0]
                    modified = speed % ((R - 1) * 2)
                    direct = 1
                    while modified:
                        if 0 <= ny + direct < R:
                            ny += direct
                        else:
                            direct = -direct
                            ny += direct
                        modified -= 1
                    if direct == -1:
                        grid[y][x][1] = 1
                    temp[ny][x].append(grid[y][x])
                elif grid[y][x][1] == 3: #오른쪽
                    nx = x
                    speed = grid[y][x][0]
                    modified = speed % ((C - 1) * 2)
                    direct = 1
                    while modified:
                        if 0 <= nx + direct < C:
                            nx += direct
                        else:
                            direct = -direct
                            nx += direct
                        modified -= 1
                    if direct == -1:
                        grid[y][x][1] = 4
                    temp[y][nx].append(grid[y][x])
                elif grid[y][x][1] == 4: #왼쪽
                    nx = x
                    speed = grid[y][x][0]
                    modified = speed % ((C - 1) * 2)
                    direct = -1
                    while modified:
                        if 0 <= nx + direct < C:
                            nx += direct
                        else:
                            direct = -direct
                            nx += direct
                        modified -= 1
                    if direct == 1:
                        grid[y][x][1] = 3
                    temp[y][nx].append(grid[y][x])
    # 먹기(상어)
    for y in range(R):
        for x in range(C):
            if temp[y][x]:
                if len(temp[y][x]) > 1:
                    check = sorted(temp[y][x], key=lambda X:X[2], reverse=True)
                    temp[y][x] = check[0]
                else:
                    temp[y][x] = temp[y][x][0]

    # 다음 페이즈
    grid[:] = temp[:]
    man += 1

print(cnt)