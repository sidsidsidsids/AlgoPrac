import sys

N, x, y, z = map(int, sys.stdin.readline().rstrip('\n').split())

maxima = max(x, y, z)
l = 1
r = maxima * N
while l <= r:
    m = (l + r) // 2
    cnt = 0
    cnt += m // x
    cnt += m // y
    cnt += m // z

    if cnt >= N:
        r = m - 1
    else:
        l = m + 1

cnt = 0
cnt += ((l - 1) // x)
cnt += ((l - 1) // y)
cnt += ((l - 1) // z)

while True:
    if l % x == 0:
        cnt += 1
        if cnt == N:
            print("A win")
            break
    if l % y == 0:
        cnt += 1
        if cnt == N:
            print("B win")
            break
    if l % z == 0:
        cnt += 1
        if cnt == N:
            print("C win")
            break
