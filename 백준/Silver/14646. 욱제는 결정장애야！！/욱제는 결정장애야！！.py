import sys

N = int(sys.stdin.readline().strip())
L = list(map(int, sys.stdin.readline().strip().split()))

maxima = -1
attach = 0
attached = set()
for l in L:
    if l in attached:
        attach -= 1
    else:
        attached.add(l)
        attach += 1
        maxima = max(attach, maxima)

print(maxima)