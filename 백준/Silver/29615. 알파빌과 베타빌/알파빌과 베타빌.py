N, M = map(int, input().split())
Ns = list(map(int, input().split()))
Ms = set(map(int, input().split()))

answer = 0
for n in range(N):
    if n >= M and Ns[n] in Ms:
        answer += 1
print(answer)