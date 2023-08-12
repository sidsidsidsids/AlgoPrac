T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int,input().split()))

    cntData = [0 for _ in range(N+1)]
    targets = [0 for _ in range(N+1)]

    for n in range(N):
        cntData[data[n]] += 1
        if cntData[data[n]] == 6:
            targets[data[n]] = 1

    cntData = [0 for _ in range(N + 1)]
    scoreTotalData = [0 for _ in range(N+1)]
    score5thData = [0 for _ in range(N+1)]
    score = 1
    for n in range(N):
        if targets[data[n]]:
            cntData[data[n]] += 1
            if cntData[data[n]] <= 4:
                scoreTotalData[data[n]] += score
                score += 1
            elif cntData[data[n]] == 5:
                score5thData[data[n]] += score
                score += 1
            else:
                score += 1

    win = 0
    scores = N*6

    for n in range(N+1):
        if targets[n]:
            if scoreTotalData[n] < scores:
                scores = scoreTotalData[n]
                win = n
            elif scoreTotalData[n] == scores and win:
                if score5thData[n] < score5thData[win]:
                    win = n
            else:
                pass
        else:
            pass

    print(win)