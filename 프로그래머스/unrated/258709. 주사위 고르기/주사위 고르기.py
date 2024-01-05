from itertools import combinations
def solution(dice):
    len_dice = len(dice)
    half_len = len_dice // 2
    if half_len == 1:
        win_1 = 0
        win_2 = 0
        for i in range(6):
            for j in range(6):
                if dice[0][i] > dice[1][j]:
                    win_1 += 1
                elif dice[0][i] < dice[1][j]:
                    win_2 += 1
        if win_1 > win_2:
            answer = [1]
        else:
            answer = [2]
        return answer
    
    arr = [n for n in range(1, len_dice + 1)]
    cases = list(combinations(arr, half_len))
    wins = 0
    
    for idx in range(len(cases) // 2):
        a_idx = cases[idx]
        b_idx = cases[-(idx+1)]
        a_win = 0
        b_win = 0
        a_rec = dict()
        b_rec = dict()
        if half_len == 2:
            for i in range(6):
                for j in range(6):
                    value = dice[a_idx[0] - 1][i] + dice[a_idx[1] - 1][j]
                    if value in a_rec:
                        a_rec[value] += 1
                    else:
                        a_rec[value] = 1
            for i in range(6):
                for j in range(6):
                    value = dice[b_idx[0] - 1][i] + dice[b_idx[1] - 1][j]
                    if value in b_rec:
                        a_win += b_rec[value][0]
                        b_win += b_rec[value][1]
                    else:
                        a_cnt = 0
                        b_cnt = 0
                        for k, v in a_rec.items():
                            if value > k:
                                b_cnt += v
                            elif value < k:
                                a_cnt += v
                        b_rec[value] = (a_cnt, b_cnt)
                        a_win += a_cnt
                        b_win += b_cnt
        elif half_len == 3:
            for i in range(6):
                for j in range(6):
                    for k in range(6):
                        value = dice[a_idx[0] - 1][i] + dice[a_idx[1] - 1][j] + dice[a_idx[2] - 1][k]
                        if value in a_rec:
                            a_rec[value] += 1
                        else:
                            a_rec[value] = 1
            for i in range(6):
                for j in range(6):
                    for k in range(6):
                        value = dice[b_idx[0] - 1][i] + dice[b_idx[1] - 1][j] + dice[b_idx[2] - 1][k]
                        if value in b_rec:
                            a_win += b_rec[value][0]
                            b_win += b_rec[value][1]
                        else:
                            a_cnt = 0
                            b_cnt = 0
                            for k, v in a_rec.items():
                                if value > k:
                                    b_cnt += v
                                elif value < k:
                                    a_cnt += v
                            b_rec[value] = (a_cnt, b_cnt)
                            a_win += a_cnt
                            b_win += b_cnt
        elif half_len == 4:
            for i in range(6):
                for j in range(6):
                    for k in range(6):
                        for l in range(6):
                            value = dice[a_idx[0] - 1][i] + dice[a_idx[1] - 1][j] + dice[a_idx[2] - 1][k] + dice[a_idx[3] - 1][l]
                            if value in a_rec:
                                a_rec[value] += 1
                            else:
                                a_rec[value] = 1
            for i in range(6):
                for j in range(6):
                    for k in range(6):
                        for l in range(6):
                            value = dice[b_idx[0] - 1][i] + dice[b_idx[1] - 1][j] + dice[b_idx[2] - 1][k] + dice[b_idx[3] - 1][l]
                            if value in b_rec:
                                a_win += b_rec[value][0]
                                b_win += b_rec[value][1]
                            else:
                                a_cnt = 0
                                b_cnt = 0
                                for k, v in a_rec.items():
                                    if value > k:
                                        b_cnt += v
                                    elif value < k:
                                        a_cnt += v
                                b_rec[value] = (a_cnt, b_cnt)
                                a_win += a_cnt
                                b_win += b_cnt
        elif half_len == 5:
            for i in range(6):
                for j in range(6):
                    for k in range(6):
                        for l in range(6):
                            for m in range(6):
                                value = dice[a_idx[0] - 1][i] + dice[a_idx[1] - 1][j] + dice[a_idx[2] - 1][k] + dice[a_idx[3] - 1][l] + dice[a_idx[4] - 1][m]
                                if value in a_rec:
                                    a_rec[value] += 1
                                else:
                                    a_rec[value] = 1
            for i in range(6):
                for j in range(6):
                    for k in range(6):
                        for l in range(6):
                            for m in range(6):
                                value = dice[b_idx[0] - 1][i] + dice[b_idx[1] - 1][j] + dice[b_idx[2] - 1][k] + dice[b_idx[3] - 1][l] + dice[b_idx[4] - 1][m] 
                                if value in b_rec:
                                    a_win += b_rec[value][0]
                                    b_win += b_rec[value][1]
                                else:
                                    a_cnt = 0
                                    b_cnt = 0
                                    for key, val in a_rec.items():
                                        if value > key:
                                            b_cnt += val
                                        elif value < key:
                                            a_cnt += val
                                    b_rec[value] = (a_cnt, b_cnt)
                                    a_win += a_cnt
                                    b_win += b_cnt
        if a_win > wins or b_win > wins:
            if a_win > b_win:
                wins = a_win
                answer = a_idx
            else:
                wins = b_win
                answer = b_idx
                            
    
    # answer = []
    return answer