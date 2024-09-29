import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())

info = dict()
weeks = M // 7

for _ in range(N):
    name, day, start, end = sys.stdin.readline().rstrip('\n').split()
    week = (int(day) - 1) // 7
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))
    time_amount = (end_h * 60 + end_m) - (start_h * 60 + start_m)
    if name in info:
        if week in info[name]:
            info[name][week]["time"] += time_amount
            info[name][week]["count"] += 1
        else:
            info[name][week] = dict()
            info[name][week]["time"] = time_amount
            info[name][week]["count"] = 1
    else:
        info[name] = dict()
        info[name][week] = dict()
        info[name][week]["time"] = time_amount
        info[name][week]["count"] = 1

answer = []
for key, val in info.items():
    flag = True
    week_cnt = 0
    for w, v in val.items():
        week_cnt += 1
        if v["time"] < 3600 or v["count"] < 5:
            flag = False
            break
    if flag and week_cnt == weeks:
        answer.append(key)

answer = sorted(answer)
if answer:
    for e in answer:
        print(e)
else:
    print(-1)