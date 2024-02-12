from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr, reverse=True)
cases = list(permutations(arr, N))
ans = 0
for case in cases:
    mass = 500
    able = True
    for elem in case:
        mass += (elem - K)
        if mass < 500:
            able = False
            break
    if able:
        ans += 1
print(ans)