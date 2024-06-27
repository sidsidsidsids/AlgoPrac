import sys
N, x = map(int,sys.stdin.readline().rstrip('\n').split())
value, _ = map(int,sys.stdin.readline().rstrip('\n').split())
for _ in range(N):
    v, _ = map(int,sys.stdin.readline().rstrip('\n').split())
    value = (value * x + v) % 1000000007
print(value)