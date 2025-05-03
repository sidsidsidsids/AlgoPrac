def locate(input_list):
    arr = []
    for idx in range(input_list[0]):
        y, x = input_list[(idx+1)*2 - 1] - 1, input_list[(idx+1)*2] - 1
        board[y][x] = -1
        arr.append((y, x))
    return arr


def check(y, x):
    if y < 0 or y > N-1 or x < 0 or x > M-1:
        return False
    if board[y][x] == 1:
        board[y][x] = 0
        return True
    elif board[y][x] == 0:
        return True
    elif board[y][x] == -1:
        return False


N, M = map(int, input().split())
board = [[1] * M for _ in range(N)]
queens = locate(list(map(int, input().split())))
knights = locate(list(map(int, input().split())))
pawns = locate(list(map(int, input().split())))

for y, x in queens:
    uu, ur, rr, rd, dd, dl, ll, lu = True, True, True, True, True, True, True, True
    for i in range(1, max(N, M)):
        if not any([uu, ur, rr, rd, dd, dl, ll, lu]):
            break
        if uu:
            res = check(y-i, x)
            if not res:
                uu = False
        if ur:
            res = check(y-i, x+i)
            if not res:
                ur = False
        if rr:
            res = check(y, x+i)
            if not res:
                rr = False
        if rd:
            res = check(y+i, x+i)
            if not res:
                rd = False
        if dd:
            res = check(y+i, x)
            if not res:
                dd = False
        if dl:
            res = check(y+i, x-i)
            if not res:
                dl = False
        if ll:
            res = check(y, x-i)
            if not res:
                ll = False
        if lu:
            res = check(y-i, x-i)
            if not res:
                lu = False

for y, x in knights:
    for ny, nx in ((y-2, x+1), (y-1, x+2), (y+1, x+2), (y+2, x+1), (y+2, x-1), (y+1, x-2), (y-1, x-2), (y-2, x-1)):
        check(ny, nx)

cnt = 0
for n in range(N):
    for m in range(M):
        if board[n][m] > 0:
            cnt += 1
print(cnt)