R, C, K = map(int,input().split())
grid = [list(input()) for _ in range(R)]
si = R-1
sj = 0
ans = 0
V = set()
V.add((si, sj))
def find(y, x, r):
    if r > K:
        return
    elif r == K:
        if y == 0 and x == C - 1:
            global ans
            ans += 1
    else:
        for ny, nx in [(y-1, x), (y+1, x), (y, x+1), (y, x-1)]:
            if 0 <= ny < R and 0 <= nx < C:
                if grid[ny][nx] == "." and (ny, nx) not in V:
                    V.add((ny, nx))
                    find(ny, nx, r+1)
                    V.remove((ny, nx))

find(si, sj, 1)
print(ans)