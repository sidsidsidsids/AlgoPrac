import sys

answer = ''
while True:
    M, N = map(int,sys.stdin.readline().rstrip('\n').split())
    if M == 0:
        break;
    grid = list(list(sys.stdin.readline().rstrip('\n')) for _ in range(M))

    V = [[0] * N for _ in range(M)]
    deposits = 0
    for m in range(M):
        for n in range(N):
            if grid[m][n] == '@' and not V[m][n]:
                Q = [(m, n)]
                deposits += 1
                while Q:
                    i, j = Q.pop()
                    V[i][j] = 1
                    for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                                   (i, j - 1), (i, j + 1),
                                   (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                        if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == '@' and not V[ni][nj]:
                            Q.append((ni, nj))
    answer += str(deposits) + "\n"
print(answer)
