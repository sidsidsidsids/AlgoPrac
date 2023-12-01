N = int(input())
room = [list(map(int,input().split())) for _ in range(N)]
professor = [0,0]
sungkyu = [0,0]
friends = []
for i in range(N):
    for j in range(N):
        if room[i][j] == 1:
            friends.append([i, j])
        elif room[i][j] == 2:
            sungkyu = [i, j]
        elif room[i][j] == 5:
            professor = [i, j]

if (professor[0] - sungkyu[0]) ** 2 + (professor[1] - sungkyu[1]) ** 2 < 25:
    print(0)
else:
    cnt = 0
    minI = min(professor[0], sungkyu[0])
    maxI = max(professor[0], sungkyu[0])
    minJ = min(professor[1], sungkyu[1])
    maxJ = max(professor[1], sungkyu[1])
    for friend in friends:
        if minI <= friend[0] <= maxI and minJ <= friend[1] <= maxJ:
            cnt += 1
    if cnt >= 3:
        print(1)
    else:
        print(0)