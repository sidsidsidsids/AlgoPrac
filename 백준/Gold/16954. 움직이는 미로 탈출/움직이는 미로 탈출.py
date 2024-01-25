import collections
maze = [list(input()) for _ in range(8)]
di = [-1, 0, 1, 0, -1, 1, 1, -1]
dj = [0, 1, 0, -1, 1, 1, -1, -1]
info = collections.deque()
info.append((7, 0))
cnt = 1
ans = 1
for move in range(9):
    if not cnt:
        ans = 0
        break
    if move == 8:
        break
    visit = set()
    while cnt:
        elem = info.popleft()
        i, j = elem[0], elem[1]
        cnt -= 1
        for idx in range(8):
            if 0 <= i + di[idx] <= 7 and 0 <= j + dj[idx] <= 7:
                if i + di[idx] - 1 >= 0 and (i+di[idx],j+dj[idx]) not in visit and maze[i + di[idx] - 1][j + dj[idx]] == "." and maze[i + di[idx]][j + dj[idx]] == ".":
                    info.append((i+di[idx],j+dj[idx]))
                    visit.add((i+di[idx],j+dj[idx]))
        if i - 1 >= 0 and (i, j) not in visit and maze[i-1][j] == ".":
            info.append((i, j))
            visit.add((i, j))
    cnt = len(info)
    tmp = [['.','.','.','.','.','.','.','.']]
    for n in range(7):
        tmp.append(maze[n])
    maze = tmp[:]
print(ans)