import sys
input = sys.stdin.readline

N = int(input())
info = dict()
arr = []
total = 0
for _ in range(N):
    loc, val = map(int,input().split())
    total += val
    arr.append((loc, val))
arr = sorted(arr, key=lambda X:X[0])
half = total / 2
tmp = 0
for elem in arr:
    tmp += elem[1]
    if tmp >= half:
        ans = elem[0]
        break
print(ans)