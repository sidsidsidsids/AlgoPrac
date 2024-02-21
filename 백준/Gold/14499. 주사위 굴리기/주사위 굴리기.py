import sys
input = sys.stdin.readline
dice = dict()
dice[1] = 0; dice[2] = 0; dice[3] = 0; dice[4] = 0; dice[5] = 0; dice[6] = 0
top = 1; front = 2; back = 5; right = 3; left = 4; bot = 6

N, M, y, x, K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
order = list(map(int,input().split()))

#    2          3
#  4 1 3      2   1
#    5          4
#    6  dice        move
def func(i, j):
    global dice
    global grid
    if grid[i][j]:
        dice[bot] = grid[i][j]
        grid[i][j] = 0
    else:
        grid[i][j] = dice[bot]
    print(dice[top])

for action in order:
    if action == 1:
        if 0 <= y < N and 0 <= x+1 < M:
            x = x + 1
            right, bot, left, top = bot, left, top, right
            func(y, x)
        else:
            pass
    elif action == 2:
        if 0 <= y < N and 0 <= x-1 < M:
            x = x - 1
            left, bot, right, top = bot, right, top, left
            func(y, x)
        else:
            pass
    elif action == 3:
        if 0 <= y-1 < N and 0 <= x < M:
            y = y - 1
            front, bot, back, top = bot, back, top, front
            func(y, x)
        else:
            pass
    elif action == 4:
        if 0 <= y+1 < N and 0 <= x < M:
            y = y + 1
            back, bot, front, top = bot, front, top, back
            func(y, x)
        else:
            pass
