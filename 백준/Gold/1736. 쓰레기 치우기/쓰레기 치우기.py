N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

trash = []
for n in range(N):
    for m in range(M):
        if grid[n][m] == 1:
            trash.append((n, m))

trash = sorted(trash, key=lambda X:(X[1], X[0]))
trash_len = len(trash)
done = [0] * trash_len
cnt = 0
for idx in range(trash_len):
    if not done[idx]:
        cnt += 1
        done[idx] = 1
        tidx = idx
        while True:
            y, x = trash[tidx][0], trash[tidx][1]
            change = False
            for nidx in range(tidx + 1, trash_len):
                if not done[nidx]:
                    if y <= trash[nidx][0] and x <= trash[nidx][1]:
                        tidx = nidx
                        done[nidx] = 1
                        change = True
                        break
            if not change:
                break
print(cnt)
