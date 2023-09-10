from itertools import permutations
n = int(input())
numbers = list(map(int,input().split()))
cases = list(permutations(numbers,n))

maxValue = 0
for case in cases:
    value = 0
    for idx in range(n-1):
        if value < maxValue // 2 and idx > n // 2:
            break
        value += abs(case[idx] - case[idx+1])
    if maxValue < value:
        maxValue = value
print(maxValue)