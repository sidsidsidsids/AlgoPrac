import sys

X = int(sys.stdin.readline().rstrip('\n'))
for x in range(X):
    printers = []
    for _ in range(3):
        printers.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
    minima = []
    for i in range(4):
        minima.append(min(printers[0][i], printers[1][i], printers[2][i]))
    total = sum(minima)
    if total < 1000000:
        print(f'Case #{x + 1}: IMPOSSIBLE')
    else:
        for i in range(4):
            total = sum(minima)
            if total > 1000000:
                if minima[i] >= total - 1000000:
                    minima[i] -= (total - 1000000)
                    break
                else:
                    minima[i] = 0
        print(f'Case #{x + 1}: {minima[0]} {minima[1]} {minima[2]} {minima[3]}')
