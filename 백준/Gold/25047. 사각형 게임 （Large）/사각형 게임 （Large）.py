import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip('\n'))
arr = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

answer = -(float("inf"))
for i in range(N + 1):
    cases = list(combinations((n for n in range(N)), i))
    for case in cases:
        target = [0] * N
        for elem in case:
            target[elem] = 1

        m = 0
        for j in range(N):
            m_tmp = 0
            j_tmp = 0
            for k in range(N):
                if target[k]:
                    m_tmp += arr[k][j]
                else:
                    j_tmp += arr[k][j]
            m += min(m_tmp, j_tmp)

        answer = max(answer, m)

print(answer)
