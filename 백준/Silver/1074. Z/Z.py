N, r, c = map(int,input().split())
cnt = -1
check = False
def Z(n, y, x):
    global cnt
    global check
    if check:
        return
    if n == 1:
        for ny, nx in [[y,x],[y,x+1],[y+1,x],[y+1,x+1]]:
            cnt += 1
            if ny == r and nx == c:
                check = True
                return
    else:
        if r < y + 2**(n-1) and c < x + 2**(n-1):
            Z(n-1, y, x)
        elif r < y + 2**(n-1) and c >= x + 2**(n-1):
            cnt += (2**(n-1))**2
            Z(n-1, y, x + 2**(n-1))
        elif r >= y + 2**(n-1) and c < x + 2**(n-1):
            cnt += ((2**(n-1))**2) * 2
            Z(n-1, y + 2**(n-1), x)
        else:
            cnt += ((2**(n-1)) ** 2) * 3
            Z(n-1,  y + 2**(n-1), x + 2**(n-1))

Z(N,0,0)
print(cnt)