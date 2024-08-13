import sys

tab = [0] * 368
space = [0] * 368
a1 = 0; a2 = 0; a3 = 0; a4 = 0; a5 = 0

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    c, s, e = sys.stdin.readline().rstrip('\n').split()
    s = int(s)
    e = int(e)
    if c == 'T':
        tab[s] += 1
        tab[e + 1] -= 1
    else:
        space[s] += 1
        space[e + 1] -= 1
    a5 = max(a5, e - s + 1)

t = 0; s = 0
for i in range(1, 367):
    t += tab[i]
    s += space[i]
    if t + s > 0:
        a1 += 1
    a2 = max(a2, t + s)
    if not t == s or (t == 0 or s == 0):
        pass
    else:
        a3 += 1
        a4 = max(a4, t + s)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)