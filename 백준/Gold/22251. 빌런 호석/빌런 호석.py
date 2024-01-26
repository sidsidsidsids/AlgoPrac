N, K, P, X = map(int,input().split())

info = dict()

info[0] = dict()
info[0][0] = [0]
info[0][1] = [8]
info[0][2] = [6,9]
info[0][3] = [2,3,5,7]
info[0][4] = [1,4]

info[1] = dict()
info[1][0] = [1]
info[1][1] = [7]
info[1][2] = [4]
info[1][3] = [3]
info[1][4] = [0,9]
info[1][5] = [2,5,8]
info[1][6] = [6]

info[2] = dict()
info[2][0] = [2]
info[2][2] = [3, 8]
info[2][3] = [0, 6, 9]
info[2][4] = [5, 7]
info[2][5] = [1, 4]

info[3] = dict()
info[3][0] = [3]
info[3][1] = [9]
info[3][2] = [2, 5, 7, 8]
info[3][3] = [0, 1, 4, 6]

info[4] = dict()
info[4][0] = [4]
info[4][2] = [1, 9]
info[4][3] = [3, 5, 7, 8]
info[4][4] = [0, 6]
info[4][5] = [2]

info[5] = dict()
info[5][0] = [5]
info[5][1] = [6, 9]
info[5][2] = [3, 8]
info[5][3] = [0, 4]
info[5][4] = [2, 7]
info[5][5] = [1]

info[6] = dict()
info[6][0] = [6]
info[6][1] = [5, 8]
info[6][2] = [0, 9]
info[6][3] = [2, 3]
info[6][4] = [4]
info[6][5] = [7]
info[6][6] = [1]

info[7] = dict()
info[7][0] = [7]
info[7][1] = [1]
info[7][2] = [3]
info[7][3] = [0, 4, 9]
info[7][4] = [2, 5, 8]
info[7][5] = [6]

info[8] = dict()
info[8][0] = [8]
info[8][1] = [0, 6, 9]
info[8][2] = [2, 3, 5]
info[8][3] = [4]
info[8][4] = [7]
info[8][5] = [1]

info[9] = dict()
info[9][0] = [9]
info[9][1] = [3, 5, 8]
info[9][2] = [0, 4, 6]
info[9][3] = [2, 7]
info[9][4] = [1]

target = [0] * K
number = str(X)
for i in range(1, len(number) + 1):
    target[-i] = int(number[-i])

answer = 0
if K == 1:
    for i in range(7):
        if i in info[target[0]] and 0 < i <= P:
            for elem in info[target[0]][i]:
                if 0 < elem <= N:
                    answer += 1
elif K == 2:
    for i in range(7):
        if i in info[target[0]] and i <= P:
            for j in range(7):
                if j in info[target[1]] and j <= P - i and i + j > 0:
                    for elem_1 in info[target[0]][i]:
                        for elem_2 in info[target[1]][j]:
                            if 0 < elem_1 * 10**1 + elem_2 * 10**0 <= N:
                                answer += 1
elif K == 3:
    for i in range(7):
        if i in info[target[0]] and i <= P:
            for j in range(7):
                if j in info[target[1]] and j <= P - i:
                    for k in range(7):
                        if k in info[target[2]] and k <= P - i - j and i + j + k > 0:
                            for elem_1 in info[target[0]][i]:
                                for elem_2 in info[target[1]][j]:
                                    for elem_3 in info[target[2]][k]:
                                        if 0 < elem_1 * 10**2 + elem_2 * 10**1 + elem_3 * 10**0 <= N:
                                            answer += 1
elif K == 4:
    for i in range(7):
        if i in info[target[0]] and i <= P:
            for j in range(7):
                if j in info[target[1]] and j <= P - i:
                    for k in range(7):
                        if k in info[target[2]] and k <= P - i - j:
                            for l in range(7):
                                if l in info[target[3]] and l <= P - i - j - k and i + j + k + l > 0:
                                    for elem_1 in info[target[0]][i]:
                                        for elem_2 in info[target[1]][j]:
                                            for elem_3 in info[target[2]][k]:
                                                for elem_4 in info[target[3]][l]:
                                                    if 0 < elem_1 * 10**3 + elem_2 * 10**2 + elem_3 * 10**1 + elem_4 * 10**0 <= N:
                                                        answer += 1
elif K == 5:
    for i in range(7):
        if i in info[target[0]] and i <= P:
            for j in range(7):
                if j in info[target[1]] and j <= P - i:
                    for k in range(7):
                        if k in info[target[2]] and k <= P - i - j:
                            for l in range(7):
                                if l in info[target[3]] and l <= P - i - j - k:
                                    for m in range(7):
                                        if m in info[target[4]] and l <= P - i - j - k - m and i + j + k + l + m > 0:
                                            for elem_1 in info[target[0]][i]:
                                                for elem_2 in info[target[1]][j]:
                                                    for elem_3 in info[target[2]][k]:
                                                        for elem_4 in info[target[3]][l]:
                                                            for elem_5 in info[target[4]][m]:
                                                                if 0 < elem_1 * 10**4 + elem_2 * 10**3 + elem_3 * 10**2 + elem_4 * 10**1 + elem_5 * 10**0 <= N:
                                                                    answer += 1
elif K == 6:
    for i in range(7):
        if i in info[target[0]] and i <= P:
            for j in range(7):
                if j in info[target[1]] and j <= P - i:
                    for k in range(7):
                        if k in info[target[2]] and k <= P - i - j:
                            for l in range(7):
                                if l in info[target[3]] and l <= P - i - j - k:
                                    for m in range(7):
                                        if m in info[target[4]] and m <= P - i - j - k - l:
                                            for n in range(7):
                                                if n in info[target[5]] and n <= P - i - j - k - l - m and i + j + k + l + m + n > 0:
                                                    for elem_1 in info[target[0]][i]:
                                                        for elem_2 in info[target[1]][j]:
                                                            for elem_3 in info[target[2]][k]:
                                                                for elem_4 in info[target[3]][l]:
                                                                    for elem_5 in info[target[4]][m]:
                                                                        for elem_6 in info[target[5]][n]:
                                                                            if 0 < elem_1 * 10**5 + elem_2 * 10**4 + elem_3 * 10**3 + elem_4 * 10**2 + elem_5 * 10**1 + elem_6 <= N:
                                                                                answer += 1
print(answer)