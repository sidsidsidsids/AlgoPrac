grid = [list(map(int,input().split())) for _ in range(10)]
answer = -1
def attach(si, sj, k):
    for i in range(si, si+k):
        for j in range(sj, sj+k):
            grid[i][j] = 0

def detach(si, sj, k):
    for i in range(si, si+k):
        for j in range(sj, sj+k):
            grid[i][j] = 1

def check(si, sj, k):
    able = True
    if si+k <= 10 and sj+k <= 10:
        for i in range(si, si+k):
            for j in range(sj, sj+k):
                if grid[i][j] == 0:
                    able = False
                    break
            if not able:
                break
    else:
        able = False
    return able

def func(a, b, c, d, e):
    global answer
    if a > 5 or b > 5 or c > 5 or d > 5 or e > 5:
        return
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                for k in range(5, 0, -1):
                    r = check(i, j, k)
                    if r == True:
                        attach(i, j, k)
                        if k == 5:
                            func(a, b, c, d, e+1)
                        elif k == 4:
                            func(a, b, c, d+1, e)
                        elif k == 3:
                            func(a, b, c+1, d, e)
                        elif k == 2:
                            func(a, b+1, c, d, e)
                        elif k == 1:
                            func(a+1, b, c, d, e)
                        detach(i, j, k)
                return
    if answer == -1:
        answer = a + b + c + d + e
    else:
        answer = min(answer, a+b+c+d+e)

func(0,0,0,0,0)
print(answer)