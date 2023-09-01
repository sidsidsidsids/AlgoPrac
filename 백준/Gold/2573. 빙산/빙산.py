from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())
iceBerg = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def isIceBergSplit():
    iceCnt = 0
    for n in range(N):
        for m in range(M):
            if iceBerg[n][m]:
                iceCnt += 1
    for i in range(1,N-1):
        for j in range(1,M-1):
            if iceBerg[i][j]:
                Q = deque()
                Q.append([i,j])
                V = [[0] * M for _ in range(N)]
                V[i][j] = 1
                cnt = 1
                while Q:
                    elems = Q.pop()
                    y, x = elems[0], elems[1]
                    for ny, nx in [[y-1,x],[y+1,x],[y,x+1],[y,x-1]]:
                        if iceBerg[ny][nx] and not V[ny][nx]:
                            Q.append([ny,nx])
                            V[ny][nx] = 1
                            cnt += 1
                if cnt != iceCnt:
                    return False
                else:
                    return True
def meltAndCheck(year):
    # 녹이는 양 체크
    meltMass = [[0] * M for _ in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if iceBerg[i][j]:
                meltMass[i][j] += [iceBerg[i-1][j], iceBerg[i+1][j], iceBerg[i][j-1], iceBerg[i][j+1]].count(0)
    # 녹이기
    for i in range(1,N-1):
        for j in range(1,M-1):
            if meltMass[i][j]:
                iceBerg[i][j] -= meltMass[i][j]
                if iceBerg[i][j] < 0:
                    iceBerg[i][j] = 0
    # 빙하 갯수 세기
    iceCnt = 0
    for n in range(N):
        for m in range(M):
            if iceBerg[n][m]:
                iceCnt += 1
    if iceCnt == 0:
        return [False, 0]
    # 빙하 DFS
    for i in range(1,N-1):
        for j in range(1,M-1):
            if iceBerg[i][j]:
                Q = deque()
                Q.append([i,j])
                V = [[0] * M for _ in range(N)]
                V[i][j] = 1
                cnt = 1
                while Q:
                    elems = Q.pop()
                    y, x = elems[0], elems[1]
                    for ny, nx in [[y-1,x],[y+1,x],[y,x+1],[y,x-1]]:
                        if iceBerg[ny][nx] and not V[ny][nx]:
                            Q.append([ny,nx])
                            V[ny][nx] = 1
                            cnt += 1
                if cnt != iceCnt:
                    return [False, year]
                else:
                    return [True, year]

check = isIceBergSplit()
if check:
    year = 1
    while year < 30000:
        result = meltAndCheck(year)
        if result[0]:
            year += 1
        else:
            year = result[1]
            break
    if year > 30000:
        print(0)
    else:
        print(year)
else:
    print(0)
