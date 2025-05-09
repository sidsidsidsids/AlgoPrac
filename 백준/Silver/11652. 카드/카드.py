N = int(input())
M = dict()
C = 0
A = 2 ** 62 + 1
for _ in range(N):
    S = int(input())
    K = M.get(S, 0)
    if K:
        M[S] += 1
    else:
        M[S] = 1
    if M[S] > C:
        C = M[S]
        A = S
    elif M[S] == C:
        A = min(A, S)
print(A)