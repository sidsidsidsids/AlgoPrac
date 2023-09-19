N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

minVal = 1000000*N

def dfs(start,cur,cnt,visit,val):
    global minVal
    if cnt == N-1:
        if grid[cur][start] and not visit[start]:
            val += grid[cur][start]
            if val < minVal:
                minVal = val
                return
    if val > minVal:
        return
    else:
        for i in range(N):
            if not visit[i]:
                if grid[cur][i]:
                    val += grid[cur][i]
                    visit[i] = 1
                    cnt += 1
                    dfs(start, i, cnt, visit, val)
                    cnt -= 1
                    visit[i] = 0
                    val -= grid[cur][i]
dfs(0, 0, 0,[0]*N,0)
print(minVal)