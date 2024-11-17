import math
S = input().rstrip('\n')
T = input().rstrip('\n')
LS = len(S)
LT = len(T)
G = math.gcd(LS, LT)
Ns = []
for n in range(1, int(math.sqrt(G)) + 1):
    if G % n == 0:
        Ns.append(n)
        if n != G / n:
            Ns.append(int(G / n))
Ns = sorted(Ns)

answer = ''
for n in Ns:
    tmp = S[:n]
    if (tmp * (LS // n) == S) and (tmp * (LT // n) == T):
        answer = tmp
        break

print(answer if answer else "No solution")