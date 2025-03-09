import math
import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

K = math.ceil(9*M/10)
HM = defaultdict(int)
answer = "NO"
for i in range(M):
    HM[A[i]] += 1
    if HM[A[i]] >= K:
        answer = "YES"
        break
if answer == "NO":
    m = M
    while m < N:
        HM[A[m-M]] -= 1
        HM[A[m]] += 1
        if HM[A[m]] >= K:
            answer = "YES"
            break
        m += 1
print(answer)