import sys

T = int(sys.stdin.readline().strip())
answers = []
for _ in range(T):
    C, V = map(int, sys.stdin.readline().strip().split())
    tastes = []
    candidates = set(n for n in range(1, C+1))
    for _ in range(V):
        tastes.append(list(map(int, sys.stdin.readline().strip().split())))
    # 1
    score = [0] * (C + 1)
    for taste in tastes:
        for elem in taste:
            if elem in candidates:
                score[elem] -= 1
                break
    score = sorted(enumerate(score), key=lambda X:X[1])
    half = V // 2
    if -score[0][1] > half:
        answers.append([score[0][0], 1])
        continue
    # 2
    candidates = {score[0][0], score[1][0]}
    score = [0] * (C + 1)
    for taste in tastes:
        for elem in taste:
            if elem in candidates:
                score[elem] -= 1
                break
    score = sorted(enumerate(score), key=lambda X: X[1])
    answers.append([score[0][0], 2])
for answer in answers:
    print(*answer)