N = int(input())

target = 3
n = 0
while target < N:
    n += 1
    target = target * 2 + n + 3

def func(total, mid, N):
    left = (total - mid) // 2
    if N <= left:
        return func(left, mid - 1, N)
    elif N > left + mid:
        return func(left, mid - 1, N - left - mid)
    else:
        if N - left == 1:
            return 'm'
        else:
            return 'o'

print(func(target, n+3, N))