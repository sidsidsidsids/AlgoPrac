L = []
S = set()
a, b = input().split()
c, d = input().split()
for e in a, b, c, d:
    L.append(e)
for i in range(4):
    for j in range(4):
        s = L[i] + " " + L[j]
        S.add(s)
T = list(S)
for e in sorted(T):
    print(e)