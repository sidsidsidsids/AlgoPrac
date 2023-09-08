r, c = map(int,input().split())
r -= 1
c -= 1
board = [list(input()) for _ in range(10)]

ableR = [True for elem in range(10)]
ableC = [True for elem in range(10)]
for i in range(10):
    for j in range(10):
        if board[i][j] == 'o':
            ableR[i] = False
            ableC[j] = False
            
ableCases = []
for elemR in range(10):
    if ableR[elemR]:
        for elemC in range(10):
            if ableC[elemC]:
                ableCases.append([elemR,elemC])

leastValue = 20
for safeR, safeC in ableCases:
    if leastValue > abs(safeR - r) + abs(safeC - c):
        leastValue = abs(safeR - r) + abs(safeC - c)
print(leastValue)