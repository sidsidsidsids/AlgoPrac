import sys
N, K = map(int,sys.stdin.readline().rstrip('\n').split())
Y = [0] * N

worst_rank = [1] * N
for _ in range(K):
    score = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    for n in range(N):
        Y[n] += score[n]
    temp = [1] * N
    for n in range(N):
        const = Y[n]
        for j in range(n):
            compare = Y[j]
            if const > compare:
                temp[j] += 1
            elif const < compare:
                temp[n] += 1
    for n in range(N):
        worst_rank[n] = max(worst_rank[n], temp[n])

minima = 1000 * (N+1)
maxima = -1000 * (N+1)
for n in range(N):
    result = Y[n]
    if result == maxima:
        max_lst.append(n+1)
    if result > maxima:
        max_lst = [n+1]
        maxima = result

for num in max_lst:
    print(f'Yodeller {num} is the TopYodeller: score {maxima}, worst rank {worst_rank[num - 1]}')