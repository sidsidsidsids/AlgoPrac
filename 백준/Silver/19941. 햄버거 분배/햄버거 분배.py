N, K = map(int,input().split())
line = list(input())

cnt = 0
for n in range(N):
    if line[n] == 'P':
        for r in range(n-K,n+K+1):
            if 0 <= r < N:
                if line[r] == 'H':
                    line[r] = 0
                    cnt += 1
                    break
print(cnt)