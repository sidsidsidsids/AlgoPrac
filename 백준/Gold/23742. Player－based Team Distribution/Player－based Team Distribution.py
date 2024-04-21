import sys
N = int(sys.stdin.readline().rstrip("\n"))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split()))
arr.sort(reverse=True)
answer = 0
value = 0
cnt = 0

for n in range(N):
    if arr[n] >= 0:
        value += arr[n]
        cnt += 1
    else:
        if (value + arr[n]) * (cnt + 1) >= (value * cnt) + arr[n]:
            value += arr[n]
            cnt += 1
        else:
            answer += arr[n]

answer += value * cnt

print(answer)