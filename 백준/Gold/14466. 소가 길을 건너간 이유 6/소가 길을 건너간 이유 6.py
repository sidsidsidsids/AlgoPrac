from collections import deque
N, K, R = map(int,input().split())
farm = [[0] * (N*2 - 1) for _ in range(N*2 - 1)]
for r in range(R):
    a,b,c,d = map(int,input().split())
    a = (a-1) * 2 ; b = (b-1) * 2 ; c = (c - 1) * 2 ; d = (d - 1) * 2
    if a == c:
        farm[a][(b+d)//2] = -1
    else:
        farm[(a+c)//2][b] = -1
for k in range(K):
    a, b = map(int,input().split())
    a = (a - 1) * 2;b = (b - 1) * 2
    farm[a][b] = 1

ans = 0
for i in range(0, N*2 - 1, 2):
    for j in range(0, N * 2 - 1, 2):
        if farm[i][j]:
            Q = deque()
            Q.append([i,j])
            V = [[0] * (N*2 - 1) for _ in range(N*2 - 1)]
            V[i][j] = 1
            cnt = 0

            while Q:
                elems = Q.popleft()
                y, x = elems[0], elems[1]
                if 0 <= y-1 < (N*2 - 1) and 0 <= x < (N*2 - 1):
                    if farm[y-1][x] == 0:
                        if not V[y-2][x]:
                            if farm[y-2][x] == 1:
                                cnt += 1
                            V[y-2][x] = 1
                            Q.append([y-2,x])
                if 0 <= y+1 < (N*2 - 1) and 0 <= x < (N*2 - 1):
                    if farm[y+1][x] == 0:
                        if not V[y+2][x]:
                            if farm[y+2][x] == 1:
                                cnt += 1
                            V[y+2][x] = 1
                            Q.append([y+2,x])
                if 0 <= y < (N*2 - 1) and 0 <= x-1 < (N*2 - 1):
                    if farm[y][x-1] == 0:
                        if not V[y][x-2]:
                            if farm[y][x-2] == 1:
                                cnt += 1
                            V[y][x-2] = 1
                            Q.append([y,x-2])
                if 0 <= y < (N*2 - 1) and 0 <= x+1 < (N*2 - 1):
                    if farm[y][x+1] == 0:
                        if not V[y][x+2]:
                            if farm[y][x+2] == 1:
                                cnt += 1
                            V[y][x+2] = 1
                            Q.append([y,x+2])
            ans += (K-1) - cnt

print(ans//2)



