import math
S = [0] * 10
N = input()
A = 0
for n in N:
    S[int(n)] += 1
    if n in ["6", '9']:
        K = math.ceil((S[6] + S[9]) / 2)
    else:
        K = S[int(n)]
    A = max(A, K)
print(A)