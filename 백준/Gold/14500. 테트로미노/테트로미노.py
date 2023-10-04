N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

def shapeA_1(y,x,grid):
    if 0 <= y and y + 3 < N:
        return grid[y][x] + grid[y+1][x] + grid[y+2][x] + grid[y+3][x]
    else:
        return 0
def shapeA_2(y,x,grid):
    if 0 <= x and x + 3 < M:
        return grid[y][x] + grid[y][x+1] + grid[y][x+2] + grid[y][x+3]
    else:
        return 0
def shapeB(y,x,grid):
    if 0 <= x and x + 1 < M and 0 <= y and y+1 < N:
        return grid[y][x] + grid[y][x+1] + grid[y+1][x] + grid[y+1][x+1]
    else:
        return 0
def shapeC_1(y,x,grid):
    if 0 <= y and y+2 < N and 0 <= x and x+1 < M:
        return max((grid[y][x] + grid[y+1][x] + grid[y+2][x] + grid[y+2][x+1]),(grid[y][x] + grid[y][x+1] + grid[y+1][x+1] + grid[y+2][x+1]), (grid[y+2][x] + grid[y+2][x+1] + grid[y+1][x+1] + grid[y][x+1]), (grid[y][x+1]+grid[y][x]+grid[y+1][x]+grid[y+2][x]))
    else:
        return 0
def shapeC_2(y,x,grid):
    if 0 <= y and y+1 < N and 0 <= x and x+2 < M:
        return max((grid[y][x] + grid[y+1][x] + grid[y][x+1] + grid[y][x+2]),(grid[y][x+2] + grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2]),(grid[y][x] + grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2]),(grid[y][x] + grid[y][x+1] + grid[y][x+2] + grid[y+1][x+2]))
    else:
        return 0
def shapeD_1(y,x,grid):
    if 0 <= y and y + 2 < N and 0<= x and x+1 < M:
        return max((grid[y][x] + grid[y+1][x] + grid[y+1][x+1] + grid[y+2][x+1]),(grid[y][x+1]+grid[y+1][x+1]+grid[y+1][x]+grid[y+2][x]))
    else:
        return 0
def shapeD_2(y,x,grid):
    if 0 <= y and y+1 < N and 0 <= x and x +2 < M:
        return max((grid[y+1][x] + grid[y+1][x+1] + grid[y][x+1] + grid[y][x+2]),(grid[y][x]+grid[y][x+1]+grid[y+1][x+1]+grid[y+1][x+2]))
    else:
        return 0
def shapeE_1(y,x,grid):
    if 0<= y and y+1 < N and 0 <= x and x+2 < M:
        return max((grid[y][x] + grid[y][x+1] + grid[y][x+2] + grid[y+1][x+1]),(grid[y][x+1] + grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2]))
    else:
        return 0
def shapeE_2(y,x,grid):
    if 0<= y and y+2 < N and 0 <= x and x+1 < M:
        return max((grid[y][x] + grid[y+1][x] + grid[y+2][x] + grid[y+1][x+1]),(grid[y][x+1] + grid[y+1][x+1] + grid[y+2][x+1] + grid[y+1][x]))
    else:
        return 0


def solution(board):
    answer = -1
    for i in range(N):
        for j in range(M):
            for check in [shapeA_1(i, j, board),shapeA_2(i, j, board),shapeB(i, j, board),shapeC_1(i, j, board),shapeC_2(i, j, board),shapeD_1(i, j, board),shapeD_2(i, j, board),shapeE_1(i, j, board),shapeE_2(i, j, board)]:
                if check > answer:
                    answer = check
    return answer


print(solution(board))
