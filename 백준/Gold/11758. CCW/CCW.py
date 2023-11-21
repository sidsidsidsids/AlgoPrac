x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

# 두 직선의 기울기로 판단
tilt1 = False
tilt2 = False
if x2 - x1 :
    tilt1 = (y2 - y1) / (x2 - x1)
if x3 - x2 :
    tilt2 = (y3 - y2) / (x3 - x2)

if tilt1 == False and tilt2 == False:
    print(0)
elif tilt1 == False:
    if y2 - y1 > 0: # 위로
        if y3 - y2 > 0:
            if x3 - x2 > 0:
                print(-1)
            elif x3 - x2 < 0:
                print(1)
            else:
                print(0)
        elif y3 - y2 < 0:
            if x3 - x2 > 0:
                print(-1)
            elif x3 - x2 < 0:
                print(1)
            else:
                print(0)
        else:
            print(0)
    elif y2 - y1 < 0: # 아래로
        if y3 - y2 > 0:
            if x3 - x2 > 0:
                print(1)
            elif x3 - x2 < 0:
                print(-1)
            else:
                print(0)
        elif y3 - y2 < 0:
            if x3 - x2 > 0:
                print(1)
            elif x3 - x2 < 0:
                print(-1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
elif tilt2 == False: # x3 - x2 == 0
    if y3 - y2 > 0: # 위로
        if y2 - y1 > 0:
            if x2 - x1 > 0:
                print(1)
            elif x2 - x1 < 0:
                print(-1)
            else:
                print(0)
        elif y2 - y1 < 0:
            if x2 - x1 > 0:
                print(1)
            elif x2 - x1 < 0:
                print(-1)
            else:
                print(0)
        else:
            print(0)
    elif y3 - y2 < 0: # 아래로
        if y2 - y1 > 0:
            if x2 - x1 > 0:
                print(-1)
            elif x2 - x1 < 0:
                print(1)
            else:
                print(0)
        elif y2 - y1 < 0:
            if x2 - x1 > 0:
                print(-1)
            elif x2 - x1 < 0:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        print(0)
else:
    if tilt1 > 0:
        if x2 > x1 and y2 > y1: #1사분면
            if tilt2 > 0:
                if x3 > x2 and y3 > y2:
                    if tilt1 > tilt2:
                        print(-1)
                    elif tilt1 < tilt2:
                        print(1)
                    else:
                        print(0)
                else:
                    if tilt1 > tilt2:
                        print(1)
                    elif tilt1 < tilt2:
                        print(-1)
                    else:
                        print(0)
            elif tilt2 < 0:
                if x3 > x2 and y3 < y2:
                    print(-1)
                else:
                    print(1)
            else:
                if x3 - x2 > 0:
                    print(-1)
                else:
                    print(1)
        else: #3사분면
            if tilt2 > 0:
                if x3 > x2 and y3 > y2:
                    if tilt1 > tilt2:
                        print(1)
                    elif tilt1 < tilt2:
                        print(-1)
                    else:
                        print(0)
                else:
                    if tilt1 > tilt2:
                        print(-1)
                    elif tilt1 < tilt2:
                        print(1)
                    else:
                        print(0)
            elif tilt2 < 0:
                if x3 > x2 and y3 < y2:
                    print(1)
                else:
                    print(-1)
            else:
                if x3 - x2 > 0:
                    print(1)
                else:
                    print(-1)
    elif tilt1 < 0:
        if x2 > x1 and y2 < y1: #2사분면
            if tilt2 > 0:
                if x3 > x2 and y3 > y2:
                    print(1)
                else:
                    print(-1)
            elif tilt2 < 0:
                if x3 > x2 and y3 < y2:
                    if tilt1 > tilt2:
                        print(-1)
                    elif tilt1 < tilt2:
                        print(1)
                    else:
                        print(0)
                else:
                    if tilt1 > tilt2:
                        print(1)
                    elif tilt1 < tilt2:
                        print(-1)
                    else:
                        print(0)
            else:
                if x3 - x2 > 0:
                    print(1)
                else:
                    print(-1)
        else: # 4사분면
            if tilt2 > 0:
                if x3 > x2 and y3 > y2:
                    print(-1)
                else:
                    print(1)
            elif tilt2 < 0:
                if x3 > x2 and y3 < y2:
                    if tilt1 > tilt2:
                        print(1)
                    elif tilt1 < tilt2:
                        print(-1)
                    else:
                        print(0)
                else:
                    if tilt1 > tilt2:
                        print(-1)
                    elif tilt1 < tilt2:
                        print(1)
                    else:
                        print(0)
            else:
                if x3 - x2 > 0:
                    print(-1)
                else:
                    print(1)
    else: # 기울기가 0
        if x2 > x1:
            if tilt2 > 0:
                if x3 > x2 and y3 > y2:
                    print(1)
                else:
                    print(-1)
            elif tilt2 < 0:
                if x3 > x2 and y3 < y2:
                    print(-1)
                else:
                    print(1)
            else:
                print(0)
        elif x2 < x1:
            if tilt2 > 0:
                if x3 > x2 and y3 > y2:
                    print(-1)
                else:
                    print(1)
            elif tilt2 < 0:
                if x3 > x2 and y3 < y2:
                    print(1)
                else:
                    print(-1)
            else:
                print(0)
        else:
            print(0)