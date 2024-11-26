import sys

Q = int(sys.stdin.readline().rstrip('\n'))
lb = 1
m = 1
arr = []
for _ in range(Q):
    q = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    t = q[0]
    if t == 0:
        lb += q[1]
    elif t == 1:
        m *= q[1]
        lb *= q[1]
    elif t == 2:
        lb += q[1] * m
    else:
        arr.append(lb)
for e in arr:
    print(e)