N = int(input())
lines = []
for _ in range(N):
    lines.append(tuple(map(int,input().split())))
lines = sorted(lines, key=lambda X:(X[0], X[1]))

INF = float('inf')
C = [INF] * (N+1)
C[0] = -INF
C[1] = lines[0][1]
tmp = 1

def b_s(l, h, n):
    if l == h:
        return l
    elif l + 1 == h:
        return l if C[l] >= n else h

    m = (l + h) // 2
    if C[m] == n:
        return m
    elif C[m] < n:
        return b_s(m+1, h, n)
    else:
        return b_s(l, m, n)

for n in range(N):
    num = lines[n][1]
    if C[tmp] < num:
        tmp += 1
        C[tmp] = num
    else:
        n_loc = b_s(0, tmp, num)
        C[n_loc] = num

print(N - tmp)