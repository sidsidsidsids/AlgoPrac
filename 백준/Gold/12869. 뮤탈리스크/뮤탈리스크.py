import sys

N = int(sys.stdin.readline().strip())
SCVs = list(map(int, sys.stdin.readline().strip().split()))
dmg = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 3, 9), (1, 9, 3)]
while len(SCVs) < 3:
    SCVs.append(0)
HPs = [[[61] * (SCVs[2] + 1) for _ in range(SCVs[1] + 1)] for _ in range(SCVs[0] + 1)]

HPs[SCVs[0]][SCVs[1]][SCVs[2]] = 0
Q = [SCVs]
while Q:
    a, b, c = Q.pop()
    for da, db, dc in dmg:
        A, B, C = max(0, a-da), max(0, b-db), max(0, c-dc)
        if HPs[a][b][c] + 1 < HPs[A][B][C]:
            HPs[A][B][C] = HPs[a][b][c] + 1
            if A or B or C:
                Q.append([A, B, C])
print(HPs[0][0][0])