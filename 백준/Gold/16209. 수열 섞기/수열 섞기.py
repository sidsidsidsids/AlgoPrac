import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

minus = []; plus = []; zero = 0
for elem in arr:
    if elem > 0:
        plus.append(elem)
    elif elem < 0:
        minus.append(elem)
    else:
        zero += 1
minus.sort()
plus.sort(reverse=True)

def func(nums):
    D = deque()
    flag = True
    D.append(nums[0])

    for i in range(1, len(nums)):
        e = nums[i]
        if flag:
            D.appendleft(e)
            flag = False
        else:
            D.append(e)
            flag = True

    return D

minus_D = func(minus) if minus else deque()
plus_D = func(plus) if plus else deque()

answer = []
if zero:
    if minus and plus:
        answer.extend(minus_D)
        answer.extend([0] * zero)
        answer.extend(plus_D)
    elif not plus:
        answer.extend(minus_D)
        answer.extend([0] * zero)
    elif not minus:
        answer.extend(plus_D)
        answer.extend([0] * zero)
else:
    if minus and plus:
        if minus_D[0] > minus_D[-1]:
            answer.extend(list(minus_D)[::-1])
        else:
            answer.extend(minus_D)
        if plus_D[0] > plus_D[-1]:
            answer.extend(list(plus_D)[::-1])
        else:
            answer.extend(plus_D)
    elif not plus:
        answer.extend(minus_D)
    elif not minus:
        answer.extend(plus_D)

print(*answer)