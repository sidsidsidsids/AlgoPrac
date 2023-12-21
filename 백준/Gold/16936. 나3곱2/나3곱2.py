N = int(input())
nums = set(map(int,input().split()))
ans = [0] * N
for n in nums:
    if (n * 2 in nums or (n // 3 in nums if n % 3 == 0 else False)) and ((n // 2 not in nums if n % 2 == 0 else True) and n * 3 not in nums):
        ans[0] = n
    elif (n * 2 not in nums and (n // 3 not in nums if n % 3 == 0 else True)) and ((n // 2 in nums if n % 2 == 0 else False) or n * 3 in nums):
        ans[N-1] = n
    if ans[0] and ans[N-1]:
        break

for idx in range(1,N-1):
    if ans[idx-1] * 2 in nums:
        ans[idx] = ans[idx-1] * 2
    elif ans[idx-1] % 3 == 0 and ans[idx-1] // 3 in nums:
        ans[idx] = ans[idx-1] // 3

print(*ans)