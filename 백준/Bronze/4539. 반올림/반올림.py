import sys
import math
N = int(sys.stdin.readline().strip())
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    K = 10
    while K <= num:
        num = math.floor(num / K + 0.5) * K
        K *= 10
    print(num)