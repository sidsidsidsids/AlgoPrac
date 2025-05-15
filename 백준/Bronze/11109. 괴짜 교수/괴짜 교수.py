T = int(input())
answers = []
for _ in range(T):
    d, n, s, p = map(int, input().split())
    par_val = d + (n*p)
    ser_val = n*s
    if par_val > ser_val:
        answers.append("do not parallelize")
    elif par_val < ser_val:
        answers.append("parallelize")
    else:
        answers.append("does not matter")
for answer in answers:
    print(answer)