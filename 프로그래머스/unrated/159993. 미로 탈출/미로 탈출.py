from collections import deque
def solution(maps):
    Y = len(maps)
    X = len(maps[0])
    for y in range(Y):
        for x in range(X):
            if maps[y][x] == 'S':
                sL = [y, x]
            elif maps[y][x] == 'L':
                lL = [y, x]
            elif maps[y][x] == 'E':
                eL = [y, x]
    
    able = False
    Q = deque()
    Q.append(sL)
    V = [[0] * X for _ in range(Y)]
    V[sL[0]][sL[1]] = 1
    lDist = 0
    
    while Q:
        elems = Q.popleft()
        i, j = elems[0], elems[1]
        for ni, nj in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
            if 0 <= ni < Y and 0 <= nj < X and maps[ni][nj] != 'X':
                if not V[ni][nj]:
                    if maps[ni][nj] == 'L':
                        lDist = V[i][j] + 1
                        break
                    else:
                        V[ni][nj] = V[i][j] + 1
                        Q.append([ni,nj])
        if lDist:
            lDist -= 1
            able = True
            break
    
    if able:
        able = False
        Q = deque()
        Q.append(lL)
        V = [[0] * X for _ in range(Y)]
        V[lL[0]][lL[1]] = 1
        eDist = 0
        
        while Q:
            elems = Q.popleft()
            i, j = elems[0], elems[1]
            for ni, nj in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
                if 0 <= ni < Y and 0 <= nj < X and maps[ni][nj] != 'X':
                    if not V[ni][nj]:
                        if maps[ni][nj] == 'E':
                            eDist = V[i][j] + 1
                            break
                        else:
                            V[ni][nj] = V[i][j] + 1
                            Q.append([ni,nj])
            if eDist:
                eDist -= 1
                able = True
                break
    
    if able:
        answer = lDist + eDist
    else:
        answer = -1
    
    return answer