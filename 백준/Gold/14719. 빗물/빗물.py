H, W = map(int,input().split())
walls = list(map(int,input().split()))
board = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i < walls[j]:
            board[i][j] = 1
ans = 0
Y = 0
X = 0
while Y < H:
    while X < W-1:
        if board[Y][X] == 1 and board[Y][X+1] == 0:
            k = 1
            while X+k < W and board[Y][X+k] == 0:
                k += 1
                if X+k == W:
                    k = 1
                    break
            ans += k - 1
            if k > 1:
                X += k - 1
            else:
                X += 1
        else:
            X += 1
    Y += 1
    X = 0
print(ans)