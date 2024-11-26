Q = int(input())
lb = 1
m = 1
for _ in range(Q):
    q = list(map(int, input().split()))
    t = q[0]
    if t == 0:
        lb += q[1]
    elif t == 1:
        m *= q[1]
        lb *= q[1]
    elif t == 2:
        lb += q[1] * m
    else:
        print(lb)