import sys
import math

n, S, W, G = map(int,sys.stdin.readline().rstrip('\n').split())
M = 4 * n - 4
board = [0] * M
board[0] = 'start'
board[n - 1] = 'island'
board[2 * n - 2] = 'fund'
board[3 * n - 3] = 'travel'
fund = 0
money = S
idx = 0
gk_idx = 0
golden_key = []
for _ in range(G):
    golden_key.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))

built = 0
for num in range(M):
    if board[num]:
        continue
    else:
        info = list(sys.stdin.readline().rstrip('\n').split())
        if info[0] == 'G':
            board[num] = 'G'
        else:
            built += 1
            board[num] = int(info[1])

I = int(sys.stdin.readline().rstrip('\n'))
logs = []
for _ in range(I):
    logs.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))

flag = True
in_island = -1
cnt_island = 3
in_travel = False
for a, b in logs:
    if in_island > -1:
        if a == b:
            in_island = -1
            continue
        in_island -= 1
        if in_island == 0:
            in_island = -1
        continue

    if in_travel:
        idx = 0
        money += W
        in_travel = False

    value = a + b
    if idx + value >= M:
        turn = math.floor((idx + value) / M)
        arrive = (idx + value) % M
        if arrive != 0:
            money += W * turn
        else:
            money += W * (turn - 1)
    else:
        arrive = idx + value
    while True:
        if arrive == 0:
            money += W
            break
        elif arrive == n - 1:
            in_island = 3
            break
        elif arrive == 2 * n - 2:
            money += fund
            fund = 0
            break
        elif arrive == 3 * n - 3:
            in_travel = True
            break
        else:
            if board[arrive] == 'G':
                gk_type, gk_value = golden_key[gk_idx]
                if gk_type == 1:
                    money += gk_value
                    gk_idx = (gk_idx + 1) % G
                    break
                elif gk_type == 2 or gk_type == 3:
                    money -= gk_value
                    if gk_type == 3:
                        fund += gk_value
                    gk_idx = (gk_idx + 1) % G
                    break
                elif gk_type == 4:
                    if arrive + gk_value >= M:
                        turn = math.floor((arrive + gk_value) / M)
                        arrive = (arrive + gk_value) % M
                        if arrive != 0:
                            money += W * turn
                        else:
                            money += W * (turn - 1)
                    else:
                        arrive = arrive + gk_value
                    gk_idx = (gk_idx + 1) % G
            else:
                price = board[arrive]
                if price:
                    if money >= price:
                        board[arrive] = 0
                        money -= price
                        built -= 1
                break

    if money < 0:
        flag = False
        break
    idx = arrive

print('WIN' if flag and not built else 'LOSE')