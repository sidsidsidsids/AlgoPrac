N, M, inventory = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]

block_total = 0
min_height = 256
for i in range(N):
    block_total += sum(grid[i])
    min_height = min(min_height, min(grid[i]))
max_height = (block_total + inventory) // (N*M)

ans_time = 256*2*(N*M)
ans_height = 0
for target in range(min_height, max_height + 1):
    val_time = 0
    for i in range(N):
        for j in range(M):
            diff = grid[i][j] - target
            if diff > 0:
                val_time += diff * 2
            elif diff < 0:
                val_time += -diff
        if val_time > ans_time:
            break
    if val_time <= ans_time:
        ans_time = val_time
        ans_height = target
print(ans_time, ans_height)

