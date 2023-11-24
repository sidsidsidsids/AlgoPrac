import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
nums = dict()
for n in range(N):
    target = int(input())
    if target in nums:
        nums[target] += 1
    else:
        nums[target] = 1
nums = sorted(nums.items(), key=lambda X:X[0])
for key, value in nums:
    for _ in range(value):
        print(key)