import math
n = int(input())
for _ in range(n):
    v = int(input())
    s = int(math.sqrt(v))
    if s*s == v:
        print(1)
    else:
        print(0)