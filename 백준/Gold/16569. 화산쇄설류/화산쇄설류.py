import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip('\n').split())
Y, X = map(int, sys.stdin.readline().rstrip('\n').split())
Y -= 1; X -= 1
land = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
volcano = []
volcas = set()
for _ in range(V):
    y, x, t = map(int, sys.stdin.readline().rstrip('\n').split())
    volcano.append([t, y-1, x-1])
    volcas.add((y-1, x-1))

visit = [[0] * M for _ in range(N)]
visit[Y][X] = 1
volcano.sort(key = lambda X:(X[0], X[1], X[2]))
v_idx = 0
dy = (1, 0, -1, 0); dx = (0, 1, 0, -1)
answer_h = land[Y][X]
answer_t = -1
time = 0
man_dq = deque(); vol_dq = deque()
man_dq.append((Y, X))
m_cnt = 1
v_cnt = 0
while True:
#   터지는 곳 추가
    if v_idx < V and volcano[v_idx][0] <= time:
        while v_idx < V and volcano[v_idx][0] <= time:
            y, x = volcano[v_idx][1], volcano[v_idx][2]
            vol_dq.append((y, x))
            visit[y][x] = 1
            v_idx += 1
            v_cnt += 1
#   화산쇄설류 덮치기 (다음 라운드 때 덮칠 곳 추가)
    v_tmp = 0
    while v_cnt:
        y, x = vol_dq.popleft()
        v_cnt -= 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx]:
                vol_dq.append((ny, nx))
                visit[ny][nx] = 1
                v_tmp += 1
    v_cnt = v_tmp
#   이동(이동하며 최대값 갱신)
#       이동 불가시 break
    m_tmp = 0
    while m_cnt:
        y, x = man_dq.popleft()
        m_cnt -= 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx] and (ny, nx) not in volcas:
                man_dq.append((ny, nx))
                visit[ny][nx] = 1
                m_tmp += 1
                height = land[ny][nx]
                if answer_h < height:
                    answer_h = height
                    answer_t = time
    if m_tmp == 0:
        break
    m_cnt = m_tmp
    time += 1

print(answer_h, answer_t + 1)