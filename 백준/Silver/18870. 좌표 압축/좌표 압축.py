N = int(input())
nums = list(map(int,input().split()))
sort_nums = sorted(nums)
k_v = dict()
num_idx = 0
for s_num in sort_nums:
    if s_num in k_v.keys():
        pass
    else:
        k_v[s_num] = num_idx
        num_idx += 1
for n in range(N):
    print(k_v[nums[n]], end=" ")