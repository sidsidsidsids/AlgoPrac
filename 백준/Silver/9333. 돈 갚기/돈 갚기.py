import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    R, B, M = map(float, sys.stdin.readline().rstrip('\n').split())
    L = B
    month = 1
    able = False
    while month <= 1200:
        x = round((L * 100) * (R / 100), 0)
        L = round(((L * 100) + x) / 100, 2)
        if L <= M:
            able = True
            break
        else:
            L -= M
            month += 1

    if able:
        print(month)
    else:
        print("impossible")