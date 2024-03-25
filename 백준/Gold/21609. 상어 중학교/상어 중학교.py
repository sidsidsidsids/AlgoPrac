N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 집합을 찾아 방문 처리를 하고 그룹 크기와 좌표들을 반환하는 함수
def find_group(y, x, v):
    global V
    mass = 1
    locs = set()
    cnt = 0
    Q = [(y, x)]
    locs.add((y, x))
    V[y][x] = 1
    while Q:
        elem = Q.pop()
        cy, cx = elem[0], elem[1]
        for ny, nx in [[cy - 1, cx], [cy, cx + 1], [cy + 1, cx], [cy, cx - 1]]:
            if 0 <= ny < N and 0 <= nx < N and (arr[ny][nx] == v or arr[ny][nx] == 0) and not V[ny][nx]:
                if (ny, nx) not in locs:
                    locs.add((ny, nx))
                    Q.append((ny, nx))
                    mass += 1
                    if arr[ny][nx] == v:
                        V[ny][nx] = 1
                    if arr[ny][nx] == 0:
                        cnt += 1
    return mass, locs, cnt

# 중력을 작용하는 함수
def gravity():
    for j in range(N):
        for i in range(N-1, -1, -1):
            if arr[i][j] > -1:
                h = i
                while h+1 < N and arr[h+1][j] == -2:
                    arr[h][j], arr[h+1][j] = -2, arr[h][j]
                    h += 1
    return

# 격자를 반시계 회전하는 함수
def turn():
    global arr
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[(N-1)-j][i] = arr[i][j]
    arr = tmp[:]
    return

score = 0
while True:
    V = [[0] * N for _ in range(N)]
    cur_group = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not V[i][j]:
                size, shape, rainbow = find_group(i, j, arr[i][j])
                cur_group.append([i, j, size, shape, rainbow])
    if not cur_group:
        break
    else:
        cur_group.sort(key=lambda x: (-x[2], -x[4], -x[0], -x[1]))

    target = cur_group[0]
    if target[2] < 2:
        break
    score += target[2] ** 2
    for grid in target[3]:
        arr[grid[0]][grid[1]] = -2
    gravity()
    turn()
    gravity()
print(score)