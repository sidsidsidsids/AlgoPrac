N, M = map(int, input().split())
l = [n for n in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    l[a-1], l[b-1] = l[b-1], l[a-1]
print(*l)