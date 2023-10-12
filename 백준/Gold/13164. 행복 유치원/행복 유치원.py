N, K = map(int,input().split())
nums = list(map(int,input().split()))
diff = [0] * (N-1)
for n in range(1, N):
    diff[n-1] = nums[n] - nums[n-1]
diff.sort(reverse=True)
print(sum(diff[K-1:]))