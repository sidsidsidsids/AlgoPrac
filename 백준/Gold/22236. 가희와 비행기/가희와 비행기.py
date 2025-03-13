import sys

D, M = map(int, sys.stdin.readline().strip().split())

if D <= 4:
    A = 1
else:
    size = D // 2 - 1
    case = [num for num in range(1, size+1)]
    K = size - 1
    while K >= 2:
        temp = [0] * K
        temp[0] = case[1]
        for i in range(1, K):
            temp[i] = (temp[i-1] + case[i+1]) % M
        case = temp[:]
        K -= 1
    A = case[-1]
print(A)