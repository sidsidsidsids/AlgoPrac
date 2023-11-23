R, C = map(int,input().split())
alphabet = [list(map(str,input())) for _ in range(R)]

alpha = [0] * 26
alpha[ord(alphabet[0][0]) - 65] = 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ans = 0
def DFS(i, j, cnt):
    global ans
    for idx in range(4):
        if 0 <= i + di[idx] < R and 0 <= j + dj[idx] < C:
            if not alpha[ord(alphabet[i+di[idx]][j+dj[idx]]) - 65]:
                alpha[ord(alphabet[i + di[idx]][j + dj[idx]]) - 65] = 1
                DFS(i+di[idx],j+dj[idx],cnt + 1)
                alpha[ord(alphabet[i + di[idx]][j + dj[idx]]) - 65] = 0
    if cnt > ans:
        ans = cnt
DFS(0,0,1)
print(ans)