import sys
T = int(sys.stdin.readline().rstrip('\n'))
answers = []
for _ in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    xp = (N * (N+1)) // 2
    l = 1
    r = 10 ** 9
    A = 1
    while l <= r:
        m = (l + r) // 2
        if (m * (m-1)) <= xp:
            A = m
            l = m + 1
        else:
            r = m - 1
    answers.append(int(A))
for answer in answers:
    print(answer)