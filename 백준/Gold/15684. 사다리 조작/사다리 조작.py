import sys
from itertools import combinations

N, M, H = map(int, sys.stdin.readline().strip().split())
ladder = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = -1

spaces = []
for h in range(H):
    for n in range(N-1):
        if not ladder[h][n] and not ladder[h][n+1]:
            spaces.append(((h, n), (h, n+1)))

def ride():
    for n in range(N):
        x = n
        for y in range(H):
            x += ladder[y][x]
        if x != n:
            return False
    return True

def add_ladder(lst):
    for left, right in lst:
        if ladder[left[0]][left[1]] or ladder[right[0]][right[1]]:
            return False
        ladder[left[0]][left[1]] = 1
        ladder[right[0]][right[1]] = -1
    return True

def rmv_ladder(lst):
    for left, right in lst:
        ladder[left[0]][left[1]] = 0
        ladder[right[0]][right[1]] = 0

able = ride()
if able:
    answer = 0
else:
    answer = -1
    for l in range(1, 4):
        cases = combinations(spaces, l)
        for case in cases:
            able_case = add_ladder(case)
            if able_case:
                check = ride()
                if check:
                    answer = l
                    break
            rmv_ladder(case)
        if answer != -1:
            break
print(answer)
