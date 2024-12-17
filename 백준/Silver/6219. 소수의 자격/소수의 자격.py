A, B, D = map(int, input().split())
D = str(D)
M = B + 1
N = [0] * M
for i in range(2, M):
    if not N[i]:
        for j in range(i+i, M, i):
            N[j] = 1
ans = 0
for n in range(A, M):
    if not N[n]:
        for s in str(n):
            if s == D:
                ans += 1
                break
print(ans)