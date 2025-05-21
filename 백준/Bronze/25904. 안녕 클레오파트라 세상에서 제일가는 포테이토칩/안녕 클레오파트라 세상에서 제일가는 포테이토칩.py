N, X = map(int, input().split())
T = list(map(int, input().split()))
k = 0
while not k:
    for n in range(N):
        if T[n] >= X:
            X += 1
            continue
        else:
            k = (n+1)
            break
print(k)