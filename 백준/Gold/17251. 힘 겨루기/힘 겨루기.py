import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

red = [0] * N
blue = [0] * N
R = 0
B = 0

red[0] = arr[0]
blue[N-1] = arr[N-1]
for i in range(1, N):
    red[i] = max(red[i-1], arr[i])
    blue[N-(i+1)] = max(blue[N-i], arr[N-(i+1)])

for i in range(1, N):
    if red[i-1] > blue[i]:
        R += 1
    elif red[i-1] < blue[i]:
        B += 1
    else:
        continue

print('R' if R > B else 'B' if B > R else 'X')