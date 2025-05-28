M = -1
L = []
for _ in range(5):
    S = list(input())
    M = max(M, len(S))
    L.append(S)
for i in range(5):
    while len(L[i]) < M:
        L[i].append(None)

A = ""
for x in range(M):
    for y in range(5):
        if L[y][x]:
            A += L[y][x]
print(A)