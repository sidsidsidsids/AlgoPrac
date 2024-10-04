import sys

T = int(sys.stdin.readline().rstrip('\n'))
for t in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    foods = []
    for _ in range(N):
        P, S = map(int, sys.stdin.readline().rstrip('\n').split())
        foods.append((P, S))
    answer = 0
    V = [0] * N

    def eat(day: int):
        global answer
        flag = True
        for n in range(N):
            if foods[n][0] >= day and not V[n]:
                flag = False
                V[n] = 1
                eat(day + foods[n][1])
                V[n] = 0
        if flag:
            answer = max(answer, day)

    eat(0)
    print(f'Case #{t+1}: {answer}')