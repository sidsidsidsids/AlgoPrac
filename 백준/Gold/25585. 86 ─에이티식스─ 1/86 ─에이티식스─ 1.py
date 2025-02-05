import sys

N = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

layer = -1
L_layer = [0, 0]
Ls = []
cur_y = -1
cur_x = -1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            Ls.append((i, j))
            L_layer[(i+j)%2] += 1
        elif grid[i][j] == 2:
            cur_y = i
            cur_x = j
            layer = (i+j)%2

if L_layer[(layer+1)%2]:
    print("Shorei")
else:
    len_L = len(Ls)
    visit = [0] * len_L
    minima = [N * len_L + 1]
    def func(y, x, time):
        if time >= minima[0]:
            return
        is_end = True
        for l in range(len_L):
            if not visit[l]:
                is_end = False
                visit[l] = 1
                func(Ls[l][0], Ls[l][1], time + max(abs(y - Ls[l][0]), abs(x - Ls[l][1])))
                visit[l] = 0
        if is_end and time < minima[0]:
            minima[0] = time

    func(cur_y, cur_x, 0)
    print("Undertaker")
    print(minima[0])