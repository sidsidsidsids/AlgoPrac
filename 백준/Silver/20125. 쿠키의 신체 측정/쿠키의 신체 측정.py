N = int(input())
grid = [str(input()) for _ in range(N)]

leftArm=0;
rightArm=0;
waist = 0;
leftLeg=0;
rightLeg=0;

for i in range(N):
    for j in range(N):
        if grid[i][j] == "*":
            heartX = j
            for ni in range(i,N):
                if grid[ni][j-1] == "*":
                    heartY = ni
                    k = 0
                    while 0 <= j-k and grid[ni][j-k] == "*":
                        k += 1
                    leftArm += k - 1
                    k = 0
                    while j+k < N and grid[ni][j+k] == "*":
                        k += 1
                    rightArm += k - 1
                    for nni in range(ni,N):
                        if grid[nni][j] == "_":
                            waist = nni - ni - 1
                            k = 0
                            while nni + k < N and grid[nni+k][j-1] == "*":
                                k += 1
                            leftLeg = k
                            k = 0
                            while nni + k < N and grid[nni+k][j+1] == "*":
                                k += 1
                            rightLeg = k
                            break
                    break
            break
    if leftArm:
        break

print(heartY+1, heartX+1)
print(leftArm,rightArm,waist,leftLeg,rightLeg)
