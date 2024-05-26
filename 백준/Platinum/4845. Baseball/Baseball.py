N = int(input())
for n in range(N):
    v_team = input()
    v_squad = []
    for _ in range(9):
        name, avg, sac = input().split()
        avg = float("0" + avg)
        sac = float("0" + sac)
        v_squad.append([name, avg, sac])
    h_team = input()
    h_squad = []
    for _ in range(9):
        name, avg, sac = input().split()
        avg = float("0" + avg)
        sac = float("0" + sac)
        h_squad.append([name, avg, sac])

    x = 1
    v_i = 0
    h_i = 0
    v_hits = 0
    v_runs = 0
    h_hits = 0
    h_runs = 0
    inning = 1
    attack = True
    record = dict()
    while inning <= 200:
        if inning == 9 and not attack and v_runs < h_runs:
            break
        elif inning > 9 and attack and v_runs != h_runs:
            break
        if inning not in record:
            record[inning] = dict()
            record[inning]['hits'] = []
            record[inning]['runs'] = []
        if attack:
            team = v_team
            squad = v_squad
            idx = v_i
        else:
            team = h_team
            squad = h_squad
            idx = h_i
        base3 = ""
        base2 = ""
        base1 = ""
        out = 0
        while out < 3:
            name, avg, sac = squad[idx]
            x = (x * 25173 + 13849) % 65536
            value = x / 65536
            if (not out and base2) or (out == 1 and base3):
                if value <= sac:
                    if base3:
                        record[inning]['runs'].append([base3, team])
                        if attack:
                            v_runs += 1
                        else:
                            h_runs += 1
                        base3 = ""
                    if base2:
                        base3 = base2
                        base2 = ""
                    if base1:
                        base2 = base1
                        base1 = ""
                out += 1
            else:
                if value <= avg:
                    record[inning]['hits'].append([name, team])
                    if attack:
                        v_hits += 1
                    else:
                        h_hits += 1
                    if base3:
                        record[inning]['runs'].append([base3, team])
                        if attack:
                            v_runs += 1
                        else:
                            h_runs += 1
                        base3 = ""
                    if base2:
                        base3 = base2
                        base2 = ""
                    if base1:
                        base2 = base1
                        base1 = ""
                    base1 = name
                else:
                    out += 1
            idx += 1
            if idx == 9:
                idx = 0
        if attack:
            attack = False
            v_i = idx
        else:
            attack = True
            h_i = idx
            inning += 1

    print(f'Game {n+1}: {v_team} vs. {h_team}')
    print()
    for key, val in record.items():
        print(f'Inning {key}:')
        print('Hits:')
        if val['hits']:
            for elem in val['hits']:
                name = elem[0].rjust(15)
                team = elem[1].rjust(15)
                print(f'  {name} {team}')
        else:
            print('  none')
        print()
        print('Runs:')
        if val['runs']:
            for elem in val['runs']:
                name = elem[0].rjust(15)
                team = elem[1].rjust(15)
                print(f'  {name} {team}')
        else:
            print('  none')
        print()
    print('End of Game:')
    print(f'  {v_team.rjust(15)} {v_runs} runs, {v_hits} hits')
    print(f'  {h_team.rjust(15)} {h_runs} runs, {h_hits} hits')

    if n != N-1:
        print("=" * 60)