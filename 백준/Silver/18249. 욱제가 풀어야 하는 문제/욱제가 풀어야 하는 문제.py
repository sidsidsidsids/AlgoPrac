import sys

mod = 10**9 + 7
arr = [0] * 191230
arr[1] = 1
arr[2] = 2
for n in range(3, 191230):
    arr[n] = (arr[n-1] + arr[n-2]) % mod

T = int(sys.stdin.readline().strip())
for _ in range(T):
    print(arr[int(sys.stdin.readline().strip())])