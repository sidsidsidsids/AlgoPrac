import sys

N = int(sys.stdin.readline().rstrip('\n'))
Xs = []
Ys = []
X = 0
Y = 0
total = 0
for _ in range(N):
    x, y, p = map(int, sys.stdin.readline().rstrip('\n').split())
    Xs.append((x, p))
    Ys.append((y, p))
    total += p
half = total / 2

Xs = sorted(Xs, key=lambda l:l[0])
Ys = sorted(Ys, key=lambda l:l[0])
cnt = 0
for x, p in Xs:
    cnt += p
    if cnt >= half:
        X = x
        break
cnt = 0
for y, p in Ys:
    cnt += p
    if cnt >= half:
        Y = y
        break
print(X, Y)