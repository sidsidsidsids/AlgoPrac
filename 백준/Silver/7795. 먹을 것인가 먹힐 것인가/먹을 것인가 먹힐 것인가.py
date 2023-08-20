T = int(input())
record = []
for _ in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    value = 0
    l = 0
    r = M-1
    aIdx = 0
    while l <= r and aIdx < N:
        if A[aIdx] > B[l]:
            value += r + 1 - l
            aIdx += 1
        else:
            while A[aIdx] <= B[l]:
                l += 1
                if l == M:
                    break
    record.append(value)

for t in range(T):
    print(record[t])
