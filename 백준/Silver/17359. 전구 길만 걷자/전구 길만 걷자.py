import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())
J = []
base = 0
for _ in range(N):
    s = sys.stdin.readline().strip()
    J.append(s)
    c = s[0]
    for e in s[1:]:
        if c != e:
            base += 1
            c = e

addition = N + 1
for case in permutations(J):
    value = 0
    for n in range(1, N):
        if case[n-1][-1] != case[n][0]:
            value += 1
            if value >= addition:
                break
    if value < addition:
        addition = value

print(base + addition)