import sys
N, M = map(int,sys.stdin.readline().rstrip('\n').split())
grid = [list(map(int,sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

value = 0
origin = set()
for n in range(N):
    for m in range(M):
        if grid[n][m]:
            value += 1
            origin.add((n, m))

answer = 0
k = 1
finish = N * M
while value < N * M:
    temp = set()
    for y, x in origin:
        for ny, nx in ((y-k, x), (y-k, x+k), (y, x+k), (y+k, x+k), (y+k, x), (y+k, x-k), (y, x-k), (y-k, x-k)):
            if 0 <= ny <= N-1 and 0 <= nx <= M-1:
                if grid[ny][nx] == 0:
                    value += 1
                grid[ny][nx] = 1
                temp.add((ny, nx))
    answer += 1
    origin = temp

print(answer)