import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)

for m in range(M):
    D, S = map(int, sys.stdin.readline().rstrip('\n').split())
    D -= 1

    if m == 0:
        cloud = [[N-1, 0], [N-2, 0], [N-1, 1], [N-2, 1]]

    vy = dy[D]
    vx = dx[D]

    # 1 ~ 2
    for elem in cloud:
        elem[0] += vy * S
        if 0 > elem[0]:
            while 0 > elem[0]:
                elem[0] += N
        elif N <= elem[0]:
            while N <= elem[0]:
                elem[0] -= N
        elem[1] += vx * S
        if 0 > elem[1]:
            while 0 > elem[1]:
                elem[1] += N
        elif N <= elem[1]:
            while N <= elem[1]:
                elem[1] -= N
        arr[elem[0]][elem[1]] += 1
    # 4 ~ 5
    clouded = set()
    for elem in cloud:
        y, x = elem
        cnt = 0
        for cy, cx in [(y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]:
            if 0 <= cy < N and 0 <= cx < N and arr[cy][cx]:
                cnt += 1
        arr[y][x] += cnt
        clouded.add((y, x))
    # 5
    cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in clouded:
                cloud.append([i, j])
                arr[i][j] -= 2
answer = 0
for i in range(N):
    for j in range(N):
        answer += arr[i][j]
print(answer)