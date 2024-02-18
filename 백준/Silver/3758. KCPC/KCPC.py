T = int(input())
for _ in range(T):
    N, K, t, M = map(int,input().split())
    arr = [[0, 0, 0] for _ in range(N+1)]
    solved = [[0] * (K+1) for _ in range(N+1)]
    for m in range(M):
        team, num, score = map(int,input().split())
        if solved[team][num]:
            if score > solved[team][num]:
                arr[team][0] += score - solved[team][num]
                solved[team][num] = score
            else:
                pass
        else:
            arr[team][0] += score
            solved[team][num] = score
        arr[team][1] += 1
        arr[team][2] = m+1
    target = arr[t][:]
    arr = sorted(arr[1:], key=lambda X:(-X[0], X[1], X[2]))
    for idx in range(N):
        if arr[idx][0] == target[0] and arr[idx][1] == target[1] and arr[idx][2] == target[2]:
            print(idx + 1)
            break
