import sys
import math

N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int,sys.stdin.readline().rstrip('\n').split()))
B = list(map(int,sys.stdin.readline().rstrip('\n').split()))
K = list(map(float, sys.stdin.readline().rstrip('\n').split()))

ad = 0
for n in range(N):
    differ = K[n] * 10
    if K[n] >= 1:
        ad += math.floor(A[n] * differ / 10)
        ad -= B[n]
    else:
        ad += A[n]
        ad -= math.floor(B[n] * differ / 10)

print(ad)