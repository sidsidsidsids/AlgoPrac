import sys

arr = [0] * 91
arr[1] = 1
arr[2] = 1
for n in range(3, 91):
    arr[n] = arr[n-2] + arr[n-1]
print(arr[int(sys.stdin.readline().strip())])