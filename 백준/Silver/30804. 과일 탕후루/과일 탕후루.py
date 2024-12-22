N = int(input())
T = list(map(int, input().split()))

D = [0] * 10
K = 0
l = 0
r = 0
A = 0
while r < N:
    elem = T[r]
    if D[elem] == 0:
        K += 1
    D[elem] += 1
    if K > 2:
        while K > 2:
            D[T[l]] -= 1
            if D[T[l]] == 0:
                K -= 1
            l += 1
    A = max(A, r - l + 1)
    r += 1
print(A)