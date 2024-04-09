import sys
N, K = map(int,sys.stdin.readline().split())
guitar = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    line, fret = map(int,sys.stdin.readline().split())
    while guitar[line] and guitar[line][-1] > fret:
        guitar[line].pop()
        cnt += 1
    if guitar[line] and guitar[line][-1] == fret:
        pass
    else:
        guitar[line].append(fret)
        cnt += 1

print(cnt)