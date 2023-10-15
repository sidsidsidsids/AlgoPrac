N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0
def devide_conquer(n, y, x):
    global white
    global blue
    if n == 1:
        if grid[y][x]:
            blue += 1
            return
        else:
            white += 1
            return
    else:
        perfection = 1
        checkP = grid[y][x]
        for ny in range(y, y+n):
            for nx in range(x, x+n):
                if grid[ny][nx] != checkP:
                    perfection = 0
                    break
            if not perfection:
                break

        if perfection:
            if checkP:
                blue += 1
                return
            else:
                white += 1
                return
        else:
            test = n // 2
            dy = y + test
            dx = x + test
            devide_conquer(test, y, x)
            devide_conquer(test, dy, x)
            devide_conquer(test, y, dx)
            devide_conquer(test, dy, dx)

devide_conquer(N,0,0)
print(white)
print(blue)