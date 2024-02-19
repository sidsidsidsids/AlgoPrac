import sys
input = sys.stdin.readline
N = int(input())
cur = list(map(int,input().split()))
goal = list(map(int,input().split()))
diff = [goal[i] - cur[i] for i in range(N)]
cnt = [0] * N
cnt[0] = abs(diff[0])
idx = 1
while idx < N:
    if diff[idx] * diff[idx - 1] > 0:
        cnt[idx] = cnt[idx-1] + max(0, abs(diff[idx]) - abs(diff[idx - 1]))
    else:
        cnt[idx] = cnt[idx-1] + abs(diff[idx])
    idx += 1
print(cnt[-1])