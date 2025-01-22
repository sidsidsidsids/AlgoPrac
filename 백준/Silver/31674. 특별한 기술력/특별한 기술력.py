import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort(reverse=True)
answer = 0
for n in range(N):
    presum = answer + arr[n]
    answer += presum
    answer %= 1000000007
print(answer)