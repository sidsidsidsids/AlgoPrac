N = int(input())
K = 2
for _ in range(N):
    K += (K-1)
print(K**2)