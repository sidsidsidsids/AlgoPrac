from collections import deque
P = int(input())
for p in range(P):
    grid = [input() for _ in range(3)]
    target = [0] * 9
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '*':
                target[i*3+j] = 1

    switch = [[0,1,3],[0,1,2,4],[1,2,5],[0,3,4,6],[1,3,4,5,7],[2,4,5,8],[3,6,7],[4,6,7,8],[5,7,8]]
    if not sum(target):
        print(0)
    else:
        Q = deque()
        Q.append([[0] * 9, [0] * 9])
        Qcnt = 1
        ans = 0
        finish = False
        while Q:
            elem = Q.popleft()
            Qcnt -= 1
            board, visit = elem[0], elem[1]
            for i in range(9):
                if not visit[i]:
                    for block in switch[i]:
                        if board[block]:
                            board[block] = 0
                        else:
                            board[block] = 1
                    visit[i] = ans + 1
                    if board[:] == target:
                        finish = True
                        break
                    newboard = board[:]
                    newvisit = visit[:]
                    Q.append([newboard, newvisit])
                    visit[i] = 0
                    for block in switch[i]:
                        if board[block]:
                            board[block] = 0
                        else:
                            board[block] = 1
            if finish:
                ans += 1
                break
            if not Qcnt:
                ans += 1
                Qcnt = len(Q)
        print(ans)