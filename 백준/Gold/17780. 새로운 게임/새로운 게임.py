from collections import deque
N, K = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(N)]
arr = [[deque() for _ in range(N)] for _ in range(N)]
order = []
for _ in range(K):
    y, x, d = list(map(int,input().split()))
    order.append([y-1, x-1, d])
for k in range(K):
    y, x, d = order[k]
    arr[y][x].append([k, d])

turn = 0
flag = False
while turn <= 1000:
    if flag:
        break
    turn += 1
    for k in range(K):
        y, x = order[k][0], order[k][1]
        if arr[y][x][-1][0] == k:
            ny, nx = y, x
            if arr[y][x][-1][1] == 1:
                nx += 1
            elif arr[y][x][-1][1] == 2:
                nx -= 1
            elif arr[y][x][-1][1] == 3:
                ny -= 1
            elif arr[y][x][-1][1] == 4:
                ny += 1

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if land[ny][nx] == 0:
                    while arr[y][x]:
                        i, d = arr[y][x].pop()
                        order[i][0], order[i][1] = ny, nx
                        arr[ny][nx].appendleft([i, d])
                elif land[ny][nx] == 1:
                    while arr[y][x]:
                        i, d = arr[y][x].popleft()
                        order[i][0], order[i][1] = ny, nx
                        arr[ny][nx].appendleft([i, d])
                elif land[ny][nx] == 2:
                    if arr[y][x][-1][1] == 1:
                        nx -= 2
                        arr[y][x][-1][1] = 2
                    elif arr[y][x][-1][1] == 2:
                        nx += 2
                        arr[y][x][-1][1] = 1
                    elif arr[y][x][-1][1] == 3:
                        ny += 2
                        arr[y][x][-1][1] = 4
                    elif arr[y][x][-1][1] == 4:
                        ny -= 2
                        arr[y][x][-1][1] = 3
                    if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
                        if land[ny][nx] == 0:
                            while arr[y][x]:
                                i, d = arr[y][x].pop()
                                order[i][0], order[i][1] = ny, nx
                                arr[ny][nx].appendleft([i, d])
                        elif land[ny][nx] == 1:
                            while arr[y][x]:
                                i, d = arr[y][x].popleft()
                                order[i][0], order[i][1] = ny, nx
                                arr[ny][nx].appendleft([i, d])
                        elif land[ny][nx] == 2:
                            pass
                if 0 <= ny <= N-1 and 0 <= nx <= N-1 and len(arr[ny][nx]) >= 4:
                    flag = True
                    break
            else:
                if arr[y][x][-1][1] == 1:
                    nx -= 2
                    arr[y][x][-1][1] = 2
                elif arr[y][x][-1][1] == 2:
                    nx += 2
                    arr[y][x][-1][1] = 1
                elif arr[y][x][-1][1] == 3:
                    ny += 2
                    arr[y][x][-1][1] = 4
                elif arr[y][x][-1][1] == 4:
                    ny -= 2
                    arr[y][x][-1][1] = 3
                if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
                    if land[ny][nx] == 0:
                        while arr[y][x]:
                            i, d = arr[y][x].pop()
                            order[i][0], order[i][1] = ny, nx
                            arr[ny][nx].appendleft([i, d])
                    elif land[ny][nx] == 1:
                        while arr[y][x]:
                            i, d = arr[y][x].popleft()
                            order[i][0], order[i][1] = ny, nx
                            arr[ny][nx].appendleft([i, d])
                    elif land[ny][nx] == 2:
                        pass
                    if len(arr[ny][nx]) >= 4:
                        flag = True
                        break
        else:
            continue

print(turn if flag else -1)
