N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input())
C = 0
for _ in range(M):
    if input() in S:
        C += 1
print(C)