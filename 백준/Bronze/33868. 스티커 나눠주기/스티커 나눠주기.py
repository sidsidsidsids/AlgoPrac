N = int(input())
T = -1
B = 5001
for _ in range(N):
    t, b = map(int, input().split())
    T = max(T, t)
    B = min(B, b)
print((T * B) % 7 + 1)