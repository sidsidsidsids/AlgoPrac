arr = list(map(int,input().split()))
len_arr = len(arr)
if len_arr == 1:
    answer = 0
else:
    inf = 4 * len_arr + 1
    dp = [[[inf] * 5 for _ in range(5)] for _ in range(len_arr - 1)]
    answer = inf

    def func(a: int, b: int):
        if a == 0:
            return 2
        else:
            if a == 1:
                if b == 2:
                    return 3
                elif b == 3:
                    return 4
                elif b == 4:
                    return 3
                else:
                    return 1
            elif a == 2:
                if b == 3:
                    return 3
                elif b == 4:
                    return 4
                elif b == 1:
                    return 3
                else:
                    return 1
            elif a == 3:
                if b == 4:
                    return 3
                elif b == 1:
                    return 4
                elif b == 2:
                    return 3
                else:
                    return 1
            elif a == 4:
                if b == 1:
                    return 3
                elif b == 2:
                    return 4
                elif b == 3:
                    return 3
                else:
                    return 1

    for i in range(len_arr):
        pos = arr[i]
        if not pos:
            break
        if i == 0:
            init_dist = func(0, pos)
            dp[i][pos][0] = init_dist
            dp[i][0][pos] = init_dist
        else:
            for a in range(5):
                for b in range(5):
                    if a != b and (a == pos or b == pos):
                        if a == pos:
                            for c in range(5):
                                dp[i][a][b] = min(dp[i-1][c][b] + func(c, a), dp[i][a][b])
                        else:
                            for c in range(5):
                                dp[i][a][b] = min(dp[i-1][a][c] + func(c, b), dp[i][a][b])

    for line in dp[len_arr-2]:
        for elem in line:
            answer = min(answer, elem)

print(answer)