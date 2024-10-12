import sys

T = int(sys.stdin.readline().rstrip('\n'))
for t in range(T):
    d = 0
    XX = [0, 0]
    YY = [0, 0]
    x = 0
    y = 0
    S = sys.stdin.readline().rstrip('\n')
    for s in S:
        if s == "F":
            if d == 0:
                y -= 1
                YY[0] = min(YY[0], y)
            elif d == 1:
                x += 1
                XX[1] = max(XX[1], x)
            elif d == 2:
                y += 1
                YY[1] = max(YY[1], y)
            elif d == 3:
                x -= 1
                XX[0] = min(XX[0], x)
        elif s == "B":
            if d == 0:
                y += 1
                YY[1] = max(YY[1], y)
            elif d == 1:
                x -= 1
                XX[0] = min(XX[0], x)
            elif d == 2:
                y -= 1
                YY[0] = min(YY[0], y)
            elif d == 3:
                x += 1
                XX[1] = max(XX[1], x)
        elif s == "R":
            if d == 0:
                d = 1
            elif d == 1:
                d = 2
            elif d == 2:
                d = 3
            elif d == 3:
                d = 0
        elif s == "L":
            if d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d = 1
            elif d == 3:
                d = 2
    print((XX[1] - XX[0]) * (YY[1] - YY[0]))