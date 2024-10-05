import sys

N = int(sys.stdin.readline().rstrip('\n'))
answers = []
info = set()
for _ in range(N):
    words = list(sys.stdin.readline().rstrip('\n'))
    target = -1
    flag = False
    L = len(words)
    for l in range(L):
        if l == 0 or (words[l] != ' ' and words[l-1] == ' '):
            if words[l].upper() not in info and words[l].lower() not in info:
                target = l
                flag = True
                info.add(words[l])
                break
    if not flag:
        for l in range(L):
            if words[l] != ' ' and words[l].upper() not in info and words[l].lower() not in info:
                target = l
                info.add(words[l])
                break

    answer = ''
    for l in range(L):
        if l == target:
            answer += "["
            answer += words[l]
            answer += "]"
        else:
            answer += words[l]
    answers.append(answer)

for answer in answers:
    print(answer)