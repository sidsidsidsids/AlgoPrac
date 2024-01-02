N = int(input())
origin = list(map(int,input()))
target = list(map(int,input()))

sample = origin[:]
sample_2 = sample[:]
for i in range(2):
    if sample_2[i] == 0:
        sample_2[i] = 1
    else:
        sample_2[i] = 0

ans = N + 1
for check in [sample, sample_2]:
    cnt = 0
    if check == sample_2:
        cnt += 1
    for n in range(1, N):
        if check[n-1] == target[n-1]:
            pass
        else:
            if check[n-1]:
                check[n-1] = 0
                if check[n]:
                    check[n] = 0
                else:
                    check[n] = 1
                if n < N-1:
                    if check[n+1]:
                        check[n+1] = 0
                    else:
                        check[n+1] = 1
            else:
                check[n-1] = 1
                if check[n]:
                    check[n] = 0
                else:
                    check[n] = 1
                if n < N-1:
                    if check[n+1]:
                        check[n+1] = 0
                    else:
                        check[n+1] = 1
            cnt += 1
    if check[-1] == target[-1]:
        if cnt < ans:
            ans = cnt
    else:
        pass

if ans == N+1:
    print(-1)
else:
    print(ans)