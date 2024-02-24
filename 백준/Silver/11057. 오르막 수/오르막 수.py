N = int(input())
nums = [1] * 10
for _ in range(N-1):
    for idx in range(9,-1,-1):
        nums[idx] += sum(nums[:idx])
print(sum(nums) % 10007)