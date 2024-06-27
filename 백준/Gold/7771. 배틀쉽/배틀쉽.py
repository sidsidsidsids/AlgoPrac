import sys
order = [list(map(int,sys.stdin.readline().rstrip('\b').split())) for _ in range(10)]
grid = [['.'] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if order[i][j] == 100:
            grid[i][j] = '#'

ships = [0, 3, 3, 2, 1]
rest = 9

def place(y, x):
    global grid
    global ships
    global rest

    if ships[4]:
        if x + 3 >= 10:
            pass
        else:
            flag = True
            for ny in range(y-1, y+2):
                if not flag:
                    break
                for nx in range(x-1, x+5):
                    if 0 <= ny <= 9 and 0 <= nx <= 9 and grid[ny][nx] == '#':
                        flag = False
                        break
            if flag:
                for nx in range(x, x+4):
                    grid[y][nx] = '#'
                ships[4] -= 1
                rest -= 1
                return
    if ships[3]:
        if x + 2 >= 10:
            pass
        else:
            flag = True
            for ny in range(y-1, y+2):
                if not flag:
                    break
                for nx in range(x-1, x+4):
                    if 0 <= ny <= 9 and 0 <= nx <= 9 and grid[ny][nx] == '#':
                        flag = False
                        break
            if flag:
                for nx in range(x, x+3):
                    grid[y][nx] = '#'
                ships[3] -= 1
                rest -= 1
                return
    if ships[2]:
        if x + 1 >= 10:
            pass
        else:
            flag = True
            for ny in range(y-1, y+2):
                if not flag:
                    break
                for nx in range(x-1, x+3):
                    if 0 <= ny <= 9 and 0 <= nx <= 9 and grid[ny][nx] == '#':
                        flag = False
                        break
            if flag:
                for nx in range(x, x+2):
                    grid[y][nx] = '#'
                ships[2] -= 1
                rest -= 1
                return
    if ships[1]:
        if x >= 10:
            pass
        else:
            flag = True
            for ny in range(y-1, y+2):
                if not flag:
                    break
                for nx in range(x-1, x+2):
                    if 0 <= ny <= 9 and 0 <= nx <= 9 and grid[ny][nx] == '#':
                        flag = False
                        break
            if flag:
                for nx in range(x, x+1):
                    grid[y][nx] = '#'
                ships[1] -= 1
                rest -= 1
                return
    return

for i in range(10):
    if not rest:
        break
    for j in range(10):
        if not rest:
            break
        if grid[i][j] == '.':
            place(i, j)

for line in grid:
    for elem in line:
        print(elem, end="")
    print()