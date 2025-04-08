import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

flag = True
inc = True

for n in range(1, N):
    if A[n-1] == A[n]:
        flag = False
        break
    elif A[n-1] < A[n]:
        if inc:
            continue
        else:
            flag = False
            break
    elif A[n-1] > A[n]:
        if inc:
            inc = False
        else:
            continue

print("YES" if flag else "NO")