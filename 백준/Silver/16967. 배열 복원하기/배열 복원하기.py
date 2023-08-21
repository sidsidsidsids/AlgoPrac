H, W, X, Y = map(int,input().split())
B = [[] for _ in range(H+X)]
for i in range(H+X):
    B[i] = list(map(int,input().split()))

LocH = X
LocW = Y
dupH = H-X
dupW = W-Y

for h in range(LocH, LocH + dupH):
    for w in range(LocW, LocW + dupW):
        # if B[h][w] != B[h-X][w-Y]:
        B[h][w] = B[h][w] - B[h-X][w-Y]

for h in range(H):
    for w in range(W):
        print(B[h][w], end=" ")
    print()