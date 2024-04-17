import sys

N = int(sys.stdin.readline())
arr = []
ans = ''
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip("\n"))

s = 0
e = N-1
while s <= e:
    if arr[s] > arr[e]:
        ans += arr[e]
        e -= 1
    elif arr[s] < arr[e]:
        ans += arr[s]
        s += 1
    else:
        i = 1
        left = True
        while s+i <= e-i:
            if arr[s+i] > arr[e-i]:
                left = False
                break
            elif arr[s+i] < arr[e-i]:
                left = True
                break
            else:
                i += 1
        if left:
            ans += arr[s]
            s += 1
        else:
            ans += arr[e]
            e -= 1

for n in range(N):
    if (n+1) % 80 == 0:
        print(ans[n], end="\n")
    else:
        print(ans[n], end="")

