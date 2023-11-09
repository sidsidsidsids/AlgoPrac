import sys
N, K = map(int,input().split())
yV = set()
xV = set()
diffV = set()
sumV = set()

ky, kx = map(int,sys.stdin.readline().split())

for k in range(K):
    y, x = map(int,sys.stdin.readline().split())
    yV.add(y)
    xV.add(x)
    diffV.add(y-x)
    sumV.add(y+x)

if ky in yV or kx in xV or ky - kx in diffV or ky + kx in sumV:
    answer = 'CHECKMATE'
    for ny, nx in [[ky - 1, kx - 1], [ky - 1, kx],[ky - 1, kx + 1], [ky, kx - 1], [ky, kx+1],[ky+1, kx - 1],[ky + 1, kx],[ky + 1, kx + 1]]:
        if 0 < ny <= N and 0 < nx <= N:
            if ny in yV or nx in xV or ny - nx in diffV or ny + nx in sumV:
                pass
            else:
                answer = 'CHECK'
                break
else:
    answer = 'STALEMATE'
    for ny, nx in [[ky - 1, kx - 1], [ky - 1, kx],[ky - 1, kx + 1], [ky, kx - 1], [ky, kx+1],[ky+1, kx - 1],[ky + 1, kx],[ky + 1, kx + 1]]:
        if 0 < ny <= N and 0 < nx <= N:
            if ny in yV or nx in xV or ny - nx in diffV or ny + nx in sumV:
                pass
            else:
                answer = 'NONE'
                break
print(answer)