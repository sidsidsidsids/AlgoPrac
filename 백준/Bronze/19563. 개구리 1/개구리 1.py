import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

if abs(a) + abs(b) <= c and not ((abs(a) + abs(b)) - c) % 2:
    print("YES")
else:
    print("NO")