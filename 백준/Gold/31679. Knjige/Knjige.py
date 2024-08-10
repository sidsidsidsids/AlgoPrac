import sys

n, t, a, b = map(int, sys.stdin.readline().rstrip('\n').split())
k = list(map(int, sys.stdin.readline().rstrip('\n').split()))
p = [0] * n
p[0] = k[0]
for i in range(1, n):
    p[i] = p[i-1] + k[i]

v = t // a
answer = 0

if n <= v:
    answer = p[n-1]
else:
    while v > 0:
        b_v = (t - a * v) // b
        if v + b_v >= n:
            if v >= n:
                answer = max(answer, p[n-1])
            else:
                answer = max(answer, p[n-1] - p[n-1 - v])
            break
        else:
            if b_v == 0:
                answer = max(answer, p[b_v + v - 1])
            else:
                answer = max(answer, p[b_v + v - 1] - p[b_v - 1])
        v -= 1

print(answer)