import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())
Q = []
P = [0] * N
D = [0] * N
I = [0] * N
for n in range(N):
    p, d, i = map(int, sys.stdin.readline().rstrip('\n').split())
    P[n], D[n], I[n] = p, d, i
    Q.append([p, d, i])
P.sort()
D.sort()
I.sort()
flag = False
answer = sys.maxsize
for p in P:
    for d in D:
        for i in I:
            value = p + d + i
            if value >= answer:
                break
            count = 0
            for qp, qd, qi in Q:
                if p >= qp and d >= qd and i >= qi:
                    count += 1
                    if count >= K and value <= answer:
                        answer = value
                        break
print(answer)