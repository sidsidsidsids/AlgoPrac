import sys

N = sys.stdin.readline().strip()
K = "abcdefghijklmnopqrstuvwxyz"
A = 0
L = len(N)
i = 0
while i < L:
    A += 1
    for k in K:
        if k == N[i]:
            i += 1
            if i == L:
                break
print(A)