N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
V = [[0] * N for _ in range(N)]
seed = 3
answer = 200 * 15 + 1
def check(i, j):
    flag = True
    if i-1 >= 0 and i+1 <= N-1 and j-1 >= 0 and j+1 <= N-1:
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i, j)]:
            if V[ni][nj]:
                flag = False
                break
    return flag

def attach(i, j):
    global seed
    seed -= 1
    cnt = 0
    for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i, j)]:
        V[ni][nj] = 1
        cnt += grid[ni][nj]
    return cnt

def detach(i, j):
    global seed
    seed += 1
    cnt = 0
    for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i, j)]:
        V[ni][nj] = 0
        cnt += grid[ni][nj]
    return cnt

def func(cost):
    global answer
    for i in range(1, N-1):
        for j in range(1, N-1):
            if seed:
                able = check(i, j)
                if able:
                    price = attach(i, j)
                    func(cost + price)
                    detach(i, j)
    if not seed:
        answer = min(answer, cost)

func(0)
print(answer)