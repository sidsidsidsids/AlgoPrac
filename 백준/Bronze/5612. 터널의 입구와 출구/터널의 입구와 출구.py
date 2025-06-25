N = int(input())
M = int(input())
A = M
flag = True
for _ in range(N):
    i, o = map(int, input().split())
    M += i - o
    A = max(A, M)
    if M < 0:
        flag = False
print(A if flag else 0)