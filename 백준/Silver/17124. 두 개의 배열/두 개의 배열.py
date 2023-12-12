T = int(input())
ans = [0] * T
for t in range(T):
    val = 0
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = sorted(A)
    B = sorted(B)
    a = 0
    b = 0

    while a < N:
        if b < M-1:
            if abs(A[a] - B[b]) > abs(A[a] - B[b+1]):
                b += 1
            else:
                val += B[b]
                a += 1
        else:
            val += B[b]
            a += 1

    ans[t] = val

for answer in ans:
    print(answer)