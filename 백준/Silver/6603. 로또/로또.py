from itertools import combinations
first = True
while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    if first:
        first = False
    else:
        print()
    k, S = arr[0], arr[1:]
    cases = list(combinations(S, 6))
    for case in cases:
        print(*case)
