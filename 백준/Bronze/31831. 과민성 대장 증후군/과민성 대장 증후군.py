N, M = map(int, input().split())
A = list(map(int, input().split()))
K = 0
C = 0
for n in range(N):
    K += A[n]
    K = max(K, 0)
    if K >= M:
        C += 1
print(C)