I = list(map(int, input().split()))
D = {}
for i in I:
    D[i] = D.get(i, 0) + 1
A = 0
M = -1
for k, v in D.items():
    if v == 3:
        A = 10000 + 1000 * k
    elif v == 2:
        A = 1000 + 100 * k
    else:
        M = max(M, k)
if not A:
    A = 100 * M
print(A)