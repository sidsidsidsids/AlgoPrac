N = 1000000
d = [0] + [1] * N
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        d[j] += i
    d[i] += d[i-1]

N = int(input())
ans = []
for _ in range(N):
    n = int(input())
    ans.append(d[n])

print('\n'.join(map(str,ans)))