n = int(input())
N = set(map(int, input().split()))
k = int(input())
answer = [0] * k
K = list(map(int, input().split()))
for i in range(k):
    if K[i] in N:
        answer[i] = 1
print(*answer)