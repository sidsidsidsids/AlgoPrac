N, K = map(int,input().split())
ab = [0] * N
ac = [0] * N
bc = [0] * N
for n in range(N):
    a, b, c = map(int,input().split())
    ab[n] = a+b
    ac[n] = a+c
    bc[n] = b+c
ab = sorted(ab,reverse=True)
ac = sorted(ac,reverse=True)
bc = sorted(bc,reverse=True)
print(max(sum(ab[:K]), sum(ac[:K]), sum(bc[:K])))