p, m = map(int,input().split())
rooms = [[] for _ in range(p)]
for idx in range(p):
    l, n = input().split()
    l = int(l)
    for room in rooms:
        if not room:
            room.append([l, n])
            break
        else:
            if len(room) < m:
                if room[0][0] - 10 <= l <= room[0][0] + 10:
                    room.append([l,n])
                    break
                else:
                    pass
            else:
                pass

for room in rooms:
    if room:
        room = sorted(room, key=lambda X: X[1])
        if len(room) == m:
            print('Started!')
            for info in room:
                print(*info)
        else:
            print('Waiting!')
            for info in room:
                print(*info)
    else:
        break