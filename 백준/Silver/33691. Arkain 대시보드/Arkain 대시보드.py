import sys

N = int(sys.stdin.readline().strip())
hm = dict()
for n in range(N):
    hm[sys.stdin.readline().strip()] = n
K = int(sys.stdin.readline().strip())
hs = set()
for k in range(K):
    hs.add(sys.stdin.readline().strip())

fixed = []
non_fixed = []
for key, val in hm.items():
    if key in hs:
        fixed.append((key, val))
    else:
        non_fixed.append((key, val))

fixed = sorted(fixed, key=lambda X:-X[1])
non_fixed = sorted(non_fixed, key=lambda X:-X[1])
for key, val in fixed + non_fixed:
    print(key)