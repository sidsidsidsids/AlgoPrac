N = int(input())
boy = list(map(int,input().split()))
girl = list(map(int,input().split()))

boy = sorted(boy, key= lambda X:abs(X))
boy_up = []
bu_len = 0
boy_down = []
bd_len = 0
for stat in boy:
    if stat > 0:
        boy_up.append(stat)
        bu_len += 1
    else:
        boy_down.append(-stat)
        bd_len += 1

girl = sorted(girl,key=lambda X:abs(X))
girl_up = []
gu_len = 0
girl_down = []
gd_len = 0
for stat in girl:
    if stat > 0:
        girl_up.append(stat)
        gu_len += 1
    else:
        girl_down.append(-stat)
        gd_len += 1

bu_idx, bd_idx, gu_idx, gd_idx = 0, 0, 0, 0
cnt = 0
if bu_len > 0 and gd_len > 0:
    while bu_idx < bu_len and gd_idx < gd_len:
        if boy_up[bu_idx] < girl_down[gd_idx]:
            cnt += 1
            bu_idx += 1
            gd_idx += 1
        else:
            gd_idx += 1
if bd_len > 0 and gu_len > 0:
    while bd_idx < bd_len and gu_idx < gu_len:
        if boy_down[bd_idx] > girl_up[gu_idx]:
            cnt += 1
            bd_idx += 1
            gu_idx += 1
        else:
            bd_idx += 1

print(cnt)