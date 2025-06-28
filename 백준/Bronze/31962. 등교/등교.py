N, X = map(int, input().split())
A = -1
for _ in range(N):
    a, b = map(int, input().split())
    if a + b <= X:
        A = max(A, a)
print(A)