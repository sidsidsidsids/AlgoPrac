import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    I, J = map(int, sys.stdin.readline().rstrip('\n').split())
    grid = [list(sys.stdin.readline().rstrip('\n')) for _ in range(I)]

    visit = [[0] * J for _ in range(I)]
    sections = 0
    spaces = 0
    for i in range(I):
        for j in range(J):
            if grid[i][j] == "." and not visit[i][j]:
                sections += 1
                spaces += 1
                S = [(i, j)]
                visit[i][j] = 1
                while S:
                    y, x = S.pop()
                    for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
                        if 0 <= ny < I and 0 <= nx < J and grid[ny][nx] == "." and not visit[ny][nx]:
                            S.append((ny, nx))
                            spaces += 1
                            visit[ny][nx] = 1

    if sections != 1:
        print(f'{sections} sections,', end=" ")
    else:
        print(f'{sections} section,', end=" ")
    if spaces != 1:
        print(f'{spaces} spaces')
    else:
        print(f'{spaces} space')
