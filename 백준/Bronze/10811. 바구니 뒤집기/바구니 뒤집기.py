N, M = map(int, input().split())
basket = [n for n in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = list(reversed(basket[i:j+1]))
    for idx in range(i, j+1):
        basket[idx] = temp[idx - i]
print(*basket[1:])