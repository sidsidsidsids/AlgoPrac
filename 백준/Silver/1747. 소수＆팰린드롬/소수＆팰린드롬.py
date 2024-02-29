nums = [0] * 1100001
nums[1] = 1
N = int(input())
for n in range(2,int(1000001**0.5)+1):
    if not nums[n]:
        param = 2
        while True:
            val = n * param
            if val > 1100000:
                break
            else:
                nums[n*param] = 1
            param += 1
while True:
    if not nums[N]:
        target = str(N)
        l = 0
        r = len(target) - 1
        is_pal = True
        while l < r:
            if target[l] == target[r]:
                l += 1
                r -= 1
            else:
                is_pal = False
                break
        if is_pal:
            break
    N += 1
print(N)