from collections import deque
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
space = []
for n in range(N):
    for m in range(M):
        if lab[n][m] == 0:
            space.append((n, m))
        elif lab[n][m] == 2:
            virus.append((n, m))

L = len(space)
max_area = L - 3
safe_area = 0
for i in range(L-2):
    i_n, i_m = space[i]
    lab[i_n][i_m] = 1
    for j in range(i+1, L-1):
        j_n, j_m = space[j]
        lab[j_n][j_m] = 1
        for k in range(j+1, L):
            k_n, k_m = space[k]
            lab[k_n][k_m] = 1
            Q = deque(virus)
            visit = [[0] * M for _ in range(N)]
            cnt = 0
            while Q:
                y, x = Q.popleft()
                for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
                    if 0 <= ny < N and 0 <= nx < M \
                        and lab[ny][nx] == 0 and not visit[ny][nx]:
                        Q.append((ny, nx))
                        visit[ny][nx] = 1
                        cnt += 1
                if max_area - cnt <= safe_area:
                    break
            safe_area = max(max_area - cnt, safe_area)
            lab[k_n][k_m] = 0
        lab[j_n][j_m] = 0
    lab[i_n][i_m] = 0
print(safe_area)