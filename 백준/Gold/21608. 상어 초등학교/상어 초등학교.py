N = int(input())
grid = [[0] * N for _ in range(N)]
prefer = [[] for _ in range(N**2)]
friends = [[] for _ in range(N**2)]

for idx in range(N**2):
    n, a, b, c, d = map(int,input().split())
    prefer[idx] = [n, a, b, c, d]
    friends[n-1] = [a, b, c, d]

for student in prefer:
    friend = [student[1], student[2], student[3], student[4]]
    loc = []
    maxcnt = -1
    maxempty = -1
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                cnt = 0
                empty = 0
                if i-1 >= 0:
                    if grid[i-1][j]:
                        if grid[i-1][j] in friend:
                            cnt += 1
                    else:
                        empty += 1
                if i+1 < N:
                    if grid[i+1][j]:
                        if grid[i+1][j] in friend:
                            cnt += 1
                    else:
                        empty += 1
                if j-1 >= 0:
                    if grid[i][j-1]:
                        if grid[i][j-1] in friend:
                            cnt += 1
                    else:
                        empty += 1
                if j+1 < N:
                    if grid[i][j+1]:
                        if grid[i][j+1] in friend:
                            cnt += 1
                    else:
                        empty += 1
                if cnt > maxcnt:
                    maxcnt = cnt
                    maxempty = empty
                    loc = [i, j]
                elif cnt == maxcnt and maxempty < empty:
                    maxempty = empty
                    loc = [i, j]
    si, sj = loc[0], loc[1]
    grid[si][sj] = student[0]

ans = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        for ay, ax in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
            if 0 <= ay < N and 0 <= ax < N:
                if grid[ay][ax] in friends[grid[y][x]-1]:
                    cnt += 1
        if not cnt:
            pass
        else:
            ans += 10**(cnt-1)
print(ans)