N, C = map(int, input().split())
s = 100 + 100 + 100 * 100 + 1
for _ in range(N):
    p, d, v = map(int, input().split())
    s = min(s, p+d+v*C)
print(s)