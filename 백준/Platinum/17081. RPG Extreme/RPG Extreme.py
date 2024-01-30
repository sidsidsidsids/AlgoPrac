turn = 0; lev = 1; hp = 20; hp_max = 20; atk = 2; arm = 2; exp = 0; exp_max = 5;
weapon = 0; armor = 0; acc = set()
boss_kill = False; result_msg = False

N, M = map(int,input().split())
grid = [list(input()) for _ in range(N)]
actions = input()
mon_cnt = 0
box_cnt = 0
for n in range(N):
    for m in range(M):
        if grid[n][m] == '&' or grid[n][m] == 'M':
            mon_cnt += 1
        elif grid[n][m] == 'B':
            box_cnt += 1
        elif grid[n][m] == '@':
            sy = n
            sx = m

mon_info = dict()
for _ in range(mon_cnt):
    R, C, S, W, A, H, E = input().split()
    mon_info[(int(R) - 1, int(C) - 1)] = [S, int(W), int(A), int(H), int(E)]

box_info = dict()
for _ in range(box_cnt):
    R, C, T, S = input().split()
    box_info[(int(R) - 1, int(C) - 1)] = [T, S]

cy = sy; cx = sx
grid[sy][sx] = "."
for act in actions:
    ny, nx = cy, cx
    if act == 'U':
        ny -= 1
    elif act == 'D':
        ny += 1
    elif act == 'L':
        nx -= 1
    elif act == 'R':
        nx += 1
    if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] != '#':
        pass
    else:
        ny, nx = cy, cx
    # 몬스터
    if grid[ny][nx] == '&' or grid[ny][nx] == 'M':
        mon_stat = mon_info[(ny, nx)]
        mon_name, mon_atk, mon_arm, mon_hp, mon_exp = mon_stat[0], mon_stat[1], mon_stat[2], mon_stat[3], mon_stat[4]
        mon_hp_tmp = mon_hp
        courage = False
        hunter = False
        if 'HU' in acc and grid[ny][nx] == 'M':
            hp = hp_max
            hunter = True
        if 'CO' in acc:
            courage = True
        while hp > 0 and mon_hp > 0:
            if courage:
                if 'DX' in acc:
                    mon_hp -= max(1, (atk + weapon) * 3 - mon_arm)
                else:
                    mon_hp -= max(1, (atk + weapon) * 2 - mon_arm)
                courage = False
            else:
                mon_hp -= max(1, (atk + weapon) - mon_arm)
            if mon_hp <= 0:
                break
            if hunter:
                hunter = False
            else:
                hp -= max(1, mon_atk - (arm + armor))
        if hp <= 0:
            if 'RE' in acc:
                ny, nx = sy, sx
                hp = hp_max
                acc.remove('RE')
                mon_hp = mon_hp_tmp
            else:
                result_msg = f'YOU HAVE BEEN KILLED BY {mon_name}..'
                hp = 0
                cy, cx = N+1, M+1
                turn += 1
                break
        else:
            if 'HR' in acc:
                hp = min(hp_max, hp + 3)
            if 'EX' in acc:
                exp += int((mon_exp * 1.2) // 1)
            else:
                exp += mon_exp
            if exp >= exp_max:
                exp_max += 5
                exp = 0
                lev += 1
                hp_max += 5
                hp = hp_max
                atk += 2
                arm += 2
            if grid[ny][nx] == 'M':
                boss_kill = True
                result_msg = 'YOU WIN!'
            grid[ny][nx] = '.'
    # 상자
    elif grid[ny][nx] == 'B':
        box_stat = box_info[(ny, nx)]
        item_type, item_stat = box_stat[0], box_stat[1]
        if item_type == 'W':
            weapon = int(item_stat)
        elif item_type == 'A':
            armor = int(item_stat)
        elif item_type == 'O':
            if item_stat not in acc and len(acc) < 4:
                acc.add(item_stat)
        grid[ny][nx] = '.'

    # 가시
    elif grid[ny][nx] == '^':
        if 'DX' in acc:
            hp -= 1
        else:
            hp -= 5
        if hp <= 0:
            if 'RE' in acc:
                ny, nx = sy, sx
                hp = hp_max
                acc.remove('RE')
            else:
                result_msg = f'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
                hp = 0
                cy, cx = N+1, M+1
                turn += 1
                break

    cy, cx = ny, nx
    turn += 1
    if boss_kill:
        break
for n in range(N):
    for m in range(M):
        if n == cy and m == cx:
            print('@', end="")
        else:
            print(grid[n][m], end="")
    print()
print(f'Passed Turns : {turn}')
print(f'LV : {lev}')
print(f'HP : {hp}/{hp_max}')
print(f'ATT : {atk}+{weapon}')
print(f'DEF : {arm}+{armor}')
print(f'EXP : {exp}/{exp_max}')
if result_msg:
    print(result_msg)
else:
    print("Press any key to continue.")