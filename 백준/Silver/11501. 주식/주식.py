T = int(input())
answers = [0] * T
for t in range(T):
    N = int(input())
    stock = list(map(int,input().split()))

    maxarr = [0] * N
    maxima = 0
    answer = 0

    for n in range(N):
        if stock[-(n+1)] > maxima:
            maxima = stock[-(n+1)]
        maxarr[-(n+1)] = maxima

    for n in range(N):
        answer += maxarr[n] - stock[n]

    answers[t] = answer

for elem in answers:
    print(elem)