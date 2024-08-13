import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    h = int(sys.stdin.readline().rstrip('\n'))
    if h > 180:
        h -= 180
    d = h // 10
    f = h % 10
    if f >= 5:
        d += 1

    if d == 0:
        print(18)
    elif d < 10:
        n = '0' + str(d)
        print(n)
    else:
        print(d)