N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
prefix = [0] * N
for n in range(N):
    v = A[n]
    if v > 0:
        prefix[n] += 1
        if n + v < N:
            prefix[n + v] -= 1
answer = 0
value = 0
for n in range(N):
    value += prefix[n]
    if value > 0:
        answer += 1
print(answer)