from collections import deque

N, M, K = map(int,input().split())
land = [[5] * N for _ in range(N)]
apply = [list(map(int,input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
tmp = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int,input().split())
    tree[x-1][y-1].append(z)

while K:
    # spring
    for y in range(N):
        for x in range(N):
            if tree[y][x]:
                change = False
                for idx in range(len(tree[y][x])):
                    if land[y][x] and land[y][x] >= tree[y][x][idx]:
                        land[y][x] -= tree[y][x][idx]
                        tree[y][x][idx] += 1
                    else:
                        for nIdx in range(idx, len(tree[y][x])):
                            tmp[y][x] += (tree[y][x][nIdx] // 2)
                        newtree = deque()
                        for tIdx in range(idx):
                            newtree.append(tree[y][x][tIdx])
                        tree[y][x] = newtree
                        break
                #     else:
                #         tmp[y][x] += (tree[y][x][idx]//2)
                #         tree[y][x][idx] = 0
                #         change = True
                # if change:
                #     newtree = deque()
                #     for elem in tree[y][x]:
                #         if elem:
                #             newtree.append(elem)
                #     tree[y][x] = newtree
    # summer
    for y in range(N):
        for x in range(N):
            if tmp[y][x]:
                land[y][x] += tmp[y][x]
                tmp[y][x] = 0
    # fall
    for y in range(N):
        for x in range(N):
            if tree[y][x]:
                for idx in range(len(tree[y][x])):
                    if tree[y][x][idx] >= 5 and not tree[y][x][idx] % 5:
                        for ny, nx in [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x-1],[y,x+1],[y+1,x-1],[y+1,x],[y+1,x+1]]:
                            if 0 <= ny < N and 0 <= nx < N:
                                tree[ny][nx].appendleft(1)
    # winter
    for y in range(N):
        for x in range(N):
            land[y][x] += apply[y][x]
    # year end
    K -= 1

cnt = 0
for y in range(N):
    for x in range(N):
        if tree[y][x]:
            cnt += len(tree[y][x])
print(cnt)
