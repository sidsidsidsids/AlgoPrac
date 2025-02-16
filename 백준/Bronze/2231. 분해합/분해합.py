import sys

N = int(sys.stdin.readline().strip())
answer = 0
for n in range(1, N):
    k = n
    num = 0
    num += k
    while k > 0:
        num += (k % 10)
        k //= 10
    if num == N:
        answer = n
        break
print(answer)