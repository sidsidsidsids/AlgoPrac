N = int(input())
A = list(map(int, input().split()))
A.sort()
i = 1
for n in range(N):
    if i < A[n]:
        break
    else:
        i += 1
print(i)