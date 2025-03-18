import sys

apartment = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    apartment[0][i] = i
for i in range(1, 15):
    for j in range(1, 15):
        for k in range(j+1):
            apartment[i][j] += apartment[i-1][k]
T = int(sys.stdin.readline().strip())
for _ in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(apartment[k][n])