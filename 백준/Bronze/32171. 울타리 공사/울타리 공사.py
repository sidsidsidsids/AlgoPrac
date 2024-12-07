N = int(input())
A = [0] * N
lx = 11
ly = 11
rx = -11
ry = -11
for n in range(N):
    a, b, c, d = map(int, input().split())
    lx, ly, rx, ry = min(lx, a), min(ly, b), max(rx, c), max(ry, d)
    A[n] = (rx - lx) * 2 + (ry - ly) * 2
for a in A:
    print(a)