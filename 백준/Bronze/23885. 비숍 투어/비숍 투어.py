N, M = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
s = sx + sy
e = ex + ey
if (max(s, e) - min(s, e)) % 2:
    print("NO")
else:
    if N == 1:
        if sy == ey:
            print("YES")
        else:
            print("NO")
    elif M == 1:
        if sx == ex:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")