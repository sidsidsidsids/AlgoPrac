a,b,c,d,e,f = map(int,input().split())
ㄱ = False
for x in range(-999,1000):
    if ㄱ:
        break
    for y in range(-999,1000):
        if a*x + b*y == c and d*x + e*y == f:
            ㄱ = True
            print(x, y)
            break