import sys

N, M = map(int, sys.stdin.readline().strip().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
WB = []
BW = []
for _ in range(4):
    WB.append(['W', 'B'] * 4)
    BW.append(['B', 'W'] * 4)
    WB.append(['B', 'W'] * 4)
    BW.append(['W', 'B'] * 4)

counter = 65

for n in range(0, N-7):
    for m in range(0, M-7):
        wb = 0
        bw = 0
        f_wb = True
        f_bw = True
        for y in range(n, n+8):
            for x in range(m, m+8):
                target = grid[y][x]
                if f_wb and WB[y-n][x-m] != target:
                    wb += 1
                if f_bw and BW[y-n][x-m] != target:
                    bw += 1
                if wb >= counter:
                    f_wb = False
                if bw >= counter:
                    f_bw = False
                if not f_wb and not f_bw:
                    break
        counter = min(counter, bw, wb)

print(counter)