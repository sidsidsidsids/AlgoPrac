N, M = map(int, input().split())
elections = [list(map(int, input().split())) for _ in range(M)]
totals = []
for i in range(N-1):
    targets = sorted((elections[m][N - 1] - elections[m][i], m+1) for m in range(M))
    prefix_sum = 0
    for j in range(M):
        prefix_sum += targets[j][0]
        if prefix_sum > 0:
            totals.append([x[1] for x in targets[j:]])
            break
    else:
        totals.append([])

L = M
LL = [m for m in range(1, M+1)]
for elem in totals:
    if len(elem) < L:
        L = len(elem)
        LL = elem

print(L)
if L > 0:
    print(*LL)