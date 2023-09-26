N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N) ]
check = [[0] * M for _ in range(N)]
cnt = 0
def air(i,j, ni, nj):
    global cnt
    while True:
        if 0 <= i+ni < N and 0 <= j+nj < M:
            i += ni
            j += nj
            if not check[i][j]:
                check[i][j] = 1
                cnt += 1
            if grid[i][j]:
                if grid[i][j] == 1:
                    if ni == 0 and nj == 1:
                        break
                    elif ni == 1 and nj == 0:
                        pass
                    elif ni == 0 and nj == -1:
                        break
                    elif ni == -1 and nj == 0:
                        pass
                elif grid[i][j] == 2:
                    if ni == 0 and nj == 1:
                        pass
                    elif ni == 1 and nj == 0:
                        break
                    elif ni == 0 and nj == -1:
                        pass
                    elif ni == -1 and nj == 0:
                        break
                elif grid[i][j] == 3:
                    if ni == 0 and nj == 1:
                        ni = -1
                        nj = 0
                    elif ni == 1 and nj == 0:
                        ni = 0
                        nj = -1
                    elif ni == 0 and nj == -1:
                        ni = 1
                        nj = 0
                    elif ni == -1 and nj == 0:
                        ni = 0
                        nj = 1
                elif grid[i][j] == 4:
                    if ni == 0 and nj == 1:
                        ni = 1
                        nj = 0
                    elif ni == 1 and nj == 0:
                        ni = 0
                        nj = 1
                    elif ni == 0 and nj == -1:
                        ni = -1
                        nj = 0
                    elif ni == -1 and nj == 0:
                        ni = 0
                        nj = -1
            else:
                pass
        else:
            break

for y in range(N):
    for x in range(M):
        if grid[y][x] == 9:
            if not check[y][x]:
                check[y][x] = 1
                cnt += 1
            air(y,x,0,1)
            air(y,x,1,0)
            air(y,x,0,-1)
            air(y,x,-1,0)

print(cnt)