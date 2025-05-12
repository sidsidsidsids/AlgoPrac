N = int(input())
M = dict()
for _ in range(N):
    e, n = map(int, input().split())
    M[e] = n
R = int(input())
answers = []
for _ in range(R):
    value = []
    L = list(map(int, input().split()))
    for elem in L[1:]:
        if elem in M:
            value.append(M[elem])
        else:
            value = ["YOU DIED"]
            break
    answers.append(value)
for answer in answers:
    print(*answer)