N = int(input())
nums = [0] * 20000001
s = list(map(int,input().split()))
for n in s:
    nums[n+10000000] += 1
M = int(input())
m = list(map(int,input().split()))
for n in m:
    print(nums[n+10000000], end=" ")
