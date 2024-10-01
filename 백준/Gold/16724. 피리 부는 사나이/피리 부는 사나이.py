import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]

grouped = set()
V = [[0] * M for _ in range(N)]
answer = 0

for n in range(N):
    for m in range(M):
        if not V[n][m]:
            y = n
            x = m
            grouping = []
            while True:
                if 0 <= y < N and 0 <= x < M:
                    cur = arr[y][x]
                    grouping.append((y, x))
                    V[y][x] = 1
                    if cur == "U":
                        y -= 1
                    elif cur == "R":
                        x += 1
                    elif cur == "D":
                        y += 1
                    elif cur == "L":
                        x -= 1
                    if 0 <= y < N and 0 <= x < M and V[y][x]:
                        if (y, x) in grouped:
                            pass
                        else:
                            answer += 1
                        for elem in grouping:
                            grouped.add(elem)
                        break
                else:
                    break

print(answer)