import sys

S = sys.stdin.readline().rstrip("\n").split()
N = int(S[0])
day, time = S[1].split("/")
h_due, m_due = time.split(":")
L = int(m_due) + int(h_due) * 60 + int(day) * 60 * 24
F = int(S[2])

info = dict()
acc_date = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

for _ in range(N):
    date, time, part, name = sys.stdin.readline().rstrip("\n").split()
    if name not in info:
        info[name] = dict()
    YY, MM, DD = date.split("-")
    hh, mm = time.split(":")
    minstamp = (acc_date[int(MM) - 1] + int(DD)) * 60 * 24 + int(hh) * 60 + int(mm)
    if part not in info[name]:
        info[name][part] = minstamp
    else:
        if info[name][part] + L < minstamp:
            if 'penalty' not in info[name]:
                info[name]['penalty'] = 0
            info[name]['penalty'] += (minstamp - (info[name][part] + L)) * F
        info[name].pop(part)

result = []
info = sorted(info.items())
for elem in info:
    if 'penalty' in elem[1]:
        result.append((elem[0], elem[1]['penalty']))

if result:
    for elem in result:
        print(*elem)
else:
    print(-1)