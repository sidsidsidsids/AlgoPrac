import sys

R, C = map(int,sys.stdin.readline().rstrip("\n").split())
grid = [list(sys.stdin.readline().rstrip("\n")) for _ in range(R)]

def func(Y, X, array):
    answer = 0
    V = [[0] * C for _ in range(R)]
    def dfs(cur_y, cur_x):
        nonlocal answer
        nonlocal V
        nonlocal flag

        if flag:
            return
        if cur_x == X-1:
            answer += 1
            flag = True
            return
        else:
            V[cur_y][cur_x] = 1
            for ny in [cur_y-1, cur_y, cur_y+1]:
                if 0 <= ny < Y and array[ny][cur_x + 1] == '.' and not V[ny][cur_x + 1]:
                    dfs(ny, cur_x + 1)
            return
    for y in range(Y):
        flag = False
        dfs(y, 0)

    return answer

print(func(R, C, grid))