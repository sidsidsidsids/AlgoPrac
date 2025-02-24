import sys

X = int(sys.stdin.readline())
for s in range(X+1, 10000):
    ls = s // 100
    rs = s % 100
    if (ls + rs) * (ls + rs) == s:
        print(s)
        break
else:
    print(-1)