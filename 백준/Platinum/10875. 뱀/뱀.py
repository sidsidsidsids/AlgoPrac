L = int(input())
N = int(input())
garo = dict()
sero = dict()
dir_y = [0, 1, 0, -1]
dir_x = [1, 0, -1, 0]
dir_i = 0
y = 0
x = 0
actions = []
for _ in range(N):
    dist, turn = input().split()
    actions.append((int(dist), turn))
actions.append((2*L + 1, 'X'))
time = 0
for act in actions:
    dist, turn = act[0], act[1]
    last = 0
    ny, nx = y + dir_y[dir_i] * dist, x + dir_x[dir_i] * dist
    # print(y,x, ' to ', ny,nx,  'dir_i: ',dir_i, 'time: ', time)
    if x != nx: # 가로
        left = min(x, nx)
        right = max(x, nx)
        if dir_i == 0:
            left += 1
        else:
            right -= 1
        for key, values in sero.items():
            if left <= key <= right:
                for value in values:
                    if min(value) <= y <= max(value):
                        if not last:
                            if dir_i == 0:
                                last = key - x
                            else:
                                last = x - key
                        else:
                            if dir_i == 0:
                                last = min(last, key - x)
                            else:
                                last = min(last, x - key)
        if y in garo:
            if dir_i == 0:
                for value in garo[y]:
                    if left <= min(value) <= right:
                        if not last:
                            last = min(value) - x
                        else:
                            last = min(last, min(value) - x)
            else:
                for value in garo[y]:
                    if left <= max(value) <= right:
                        if not last:
                            last = x - max(value)
                        else:
                            last = min(last, x - max(value))
        if last:
            time += last
            break
        if nx < -L or L < nx:
            if dir_i == 0:
                last = L - x
            else:
                last = x - (-L)
            time += last + 1
            break
        time += dist
        if y not in garo:
            garo[y] = []
        garo[y].append((x, nx))
        y, x = ny, nx
        if turn == 'R':
            dir_i += 1
            if dir_i == 4:
                dir_i = 0
        else:
            dir_i -= 1
            if dir_i == -1:
                dir_i = 3
    else: # 세로
        left = min(y, ny)
        right = max(y, ny)
        if dir_i == 1:
            left += 1
        else:
            right -= 1
        for key, values in garo.items():
            if left <= key <= right:
                for value in values:
                    if min(value) <= x <= max(value):
                        if not last:
                            if dir_i == 1:
                                last = key - y
                            else:
                                last = y - key
                        else:
                            if dir_i == 1:
                                last = min(last, key - y)
                            else:
                                last = min(last, y - key)
        if x in sero:
            if dir_i == 1:
                for value in sero[x]:
                    if left <= min(value) <= right:
                        if not last:
                            last = min(value) - y
                        else:
                            last = min(last, min(value) - y)
            else:
                for value in sero[x]:
                    if left <= max(value) <= right:
                        if not last:
                            last = y - max(value)
                            print(value)
                        else:
                            last = min(last, y - max(value))
        if last:
            time += last
            break
        if ny < -L or L < ny:
            if dir_i == 1:
                last = L - y
            else:
                last = y - (-L)
            time += last + 1
            break
        time += dist
        if x not in sero:
            sero[x] = []
        sero[x].append((y, ny))
        y, x = ny, nx
        if turn == 'R':
            dir_i += 1
            if dir_i == 4:
                dir_i = 0
        else:
            dir_i -= 1
            if dir_i == -1:
                dir_i = 3
print(time)