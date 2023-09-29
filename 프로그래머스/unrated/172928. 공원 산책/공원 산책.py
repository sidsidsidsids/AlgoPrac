def solution(park, routes):
    Y = len(park)
    X = len(park[0])
    for y in range(Y):
        for x in range(X):
            if park[y][x] == 'S':
                sy = y
                sx = x
                break
    for route in routes:
        if route[0] == 'N':
            if 0 <= sy - int(route[2]) < Y:
                able = True
                for ny in range(sy,sy-int(route[2])-1,-1):
                    if park[ny][sx] == 'X':
                        able = False
                        break
                if able:
                    sy = sy - int(route[2])
            else:
                pass
        elif route[0] == 'S':
            if 0 <= sy + int(route[2]) < Y:
                able = True
                for ny in range(sy,sy+int(route[2])+1):
                    if park[ny][sx] == 'X':
                        able = False
                        break
                if able:
                    sy = sy + int(route[2])
            else:
                pass
        elif route[0] == 'W':
            if 0 <= sx - int(route[2]) < X:
                able = True
                for nx in range(sx,sx-int(route[2])-1,-1):
                    if park[sy][nx] == 'X':
                        able = False
                        break
                if able:
                    sx = sx - int(route[2])
            else:
                pass
        else:
            if 0 <= sx + int(route[2]) < X:
                able = True
                for nx in range(sx,sx+int(route[2])+1):
                    if park[sy][nx] == 'X':
                        able = False
                        break
                if able:
                    sx = sx + int(route[2])
            else:
                pass
    return [sy, sx]