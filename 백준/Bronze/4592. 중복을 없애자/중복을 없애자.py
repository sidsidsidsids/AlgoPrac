answers = []
while True:
    Q = list(map(int, input().split()))
    if Q[0] == 0:
        break
    K = -1
    answer = []
    for e in Q[1:]:
        if e != K:
            answer.append(e)
            K = e
    answer.append("$")
    answers.append(answer)
for answer in answers:
    print(*answer)