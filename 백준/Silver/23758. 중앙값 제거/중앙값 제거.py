import sys
import math
N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))
A = sorted(A)
mid = (len(A) + 1) // 2 - 1
cnt = 1
for i in range(mid + 1):
    cnt += int(math.log2(A[i]))
print(cnt)