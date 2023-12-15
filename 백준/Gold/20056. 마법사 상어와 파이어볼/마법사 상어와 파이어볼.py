N, M, K = map(int,input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,m,s,d = map(int,input().split()) #위치, 질량, 속력, 방향
    grid[r-1][c-1].append([m,s,d])

for _ in range(K): # K번 명령
    move = [[[] for _ in range(N)] for _ in range(N)]
    # 1. 이동
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                for elem in grid[i][j]:
                    if elem[2] % 2 == 0:
                        if elem[2] == 0:
                            ni = i - elem[1] % N
                            if ni < 0:
                                ni += N
                            move[ni][j].append(elem)
                        elif elem[2] == 4:
                            ni = i + elem[1] % N
                            if ni > N-1:
                                ni -= N
                            move[ni][j].append(elem)
                        elif elem[2] == 6:
                            nj = j - elem[1] % N
                            if nj < 0:
                                nj += N
                            move[i][nj].append(elem)
                        elif elem[2] == 2:
                            nj = j + elem[1] % N
                            if nj > N-1:
                                nj -= N
                            move[i][nj].append(elem)
                    else:
                        if elem[2] == 1:
                            ni = i - elem[1] % N
                            if ni < 0:
                                ni += N
                            nj = j + elem[1] % N
                            if nj > N-1:
                                nj -= N
                            move[ni][nj].append(elem)
                        elif elem[2] == 3:
                            ni = i + elem[1] % N
                            if ni > N-1:
                                ni -= N
                            nj = j + elem[1] % N
                            if nj > N - 1:
                                nj -= N
                            move[ni][nj].append(elem)
                        elif elem[2] == 5:
                            ni = i + elem[1] % N
                            if ni > N-1:
                                ni -= N
                            nj = j - elem[1] % N
                            if nj < 0:
                                nj += N
                            move[ni][nj].append(elem)
                        elif elem[2] == 7:
                            ni = i - elem[1] % N
                            if ni < 0:
                                ni += N
                            nj = j - elem[1] % N
                            if nj < 0:
                                nj += N
                            move[ni][nj].append(elem)
    # 2
    for i in range(N):
        for j in range(N):
            if move[i][j] and len(move[i][j]) >= 2:
                m_amount = 0
                s_amount = 0
                cnt = 0
                odd = True
                even = True
                for elem in move[i][j]:
                    m_amount += elem[0]
                    s_amount += elem[1]
                    cnt += 1
                    if elem[2] % 2 == 0:
                        odd = False
                    else:
                        even = False
                adj_m = m_amount // 5
                adj_s = s_amount // cnt
                if adj_m > 0:
                    if odd or even:
                        move[i][j] = [[adj_m, adj_s, 0],[adj_m, adj_s, 2],[adj_m, adj_s, 4],[adj_m, adj_s, 6]]
                    else:
                        move[i][j] = [[adj_m, adj_s, 1], [adj_m, adj_s, 3], [adj_m, adj_s, 5], [adj_m, adj_s, 7]]
                else:
                    move[i][j] = []

    grid[:] = move[:]

ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for elem in grid[i][j]:
                ans += elem[0]

print(ans)