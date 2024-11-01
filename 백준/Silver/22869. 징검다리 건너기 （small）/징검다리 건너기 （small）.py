import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))

V = [0] * N
V[0] = 1
S = [0]
flag = False
while S:
    if flag:
        break
    i = S.pop()
    for j in range(i+1, N):
        if j-i > K:
            break
        if not V[j] and ((j - i) * (1 + abs(A[j] - A[i]))) <= K:
            S.append(j)
            V[j] = 1
            if j == N-1:
                flag = True
                break

print("YES" if flag else "NO")