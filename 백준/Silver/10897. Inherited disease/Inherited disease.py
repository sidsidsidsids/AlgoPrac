import sys

D = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

cnt = 0
cur = 1
node = 1
mod = 1000000007

for i in range(1, D+1):
    cur = ((cur - 1) * i + arr[i-1]) % mod
    print((cnt + cur) % mod)
    node = (node * i) % mod
    cnt = (cnt + node) % mod