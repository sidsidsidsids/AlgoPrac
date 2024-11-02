import sys

N, L = map(int, sys.stdin.readline().rstrip('\n').split())
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))
A.sort()
for a in A:
    if a <= L:
        L += 1
    else:
        break
print(L)