N, M = map(int, input().split())
Q = list(map(int, input().split()))
maxima = -1
target = 100001
for _ in range(M):
    L = list(input().split())
    score = 0
    for i in range(N):
        if L[i+1] == "O":
            score += Q[i]
    if score >= maxima:
        if score > maxima:
            target = int(L[0])
        else:
            target = min(int(L[0]), target)
        maxima = score
print(target, maxima)