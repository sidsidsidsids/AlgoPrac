N, M = map(int,input().split())
grid = [list(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == '.':
            if (j - 1 < 0 or grid[i][j-1] == '#') and (j + 2 < M and grid[i][j+1] != '#' and grid[i][j+2] != '#'):
                    grid[i][j] = '!'
                    cnt += 1
            elif (i-1 < 0 or grid[i-1][j] == '#') and (i + 2 < N and grid[i+1][j] != '#' and grid[i+2][j] != '#'):
                    grid[i][j] = '!'
                    cnt += 1

print(cnt)
for i in range(N):
    for j in range(M):
        if grid[i][j] == '!':
            print(i+1, j+1)