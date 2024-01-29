N, M = map(int,input().split())
arr = [0] * N
for n in range(N):
    P, L = map(int,input().split())
    cur = list(map(int,input().split()))
    if P < L:
        arr[n] = 1
    else:
        cur = sorted(cur)
        arr[n] = cur[-L]
arr = sorted(arr)
ans = 0
for n in range(N):
    if M >= arr[n]:
        M -= arr[n]
        ans += 1
    else:
        break
print(ans)