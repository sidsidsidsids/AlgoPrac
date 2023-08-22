N = int(input())
dots = []
minY = 1000
maxY = -1000
minX = 1000
maxX = -1000

for n in range(N):
    y,x = map(int,input().split())
    if y < minY:
        minY = y
    if y > maxY:
        maxY = y
    if x < minX:
        minX = x
    if x > maxX:
        maxX = x
    dots.append([y,x])

squareLen = max(abs(maxY - minY), abs(maxX - minX))
cnt = 0
for i, j in dots:
    if (i == minY and minX <= j <= minX + squareLen) or (i == minY + squareLen and minX <= j <= minX + squareLen) or (minY <= i <= minY + squareLen and j == minX) or (minY <= i <= minY + squareLen and j == minX + squareLen):
        pass
    else:
        cnt += 1
        break
for i, j in dots:
    if (i == minY and maxX - squareLen <= j <= maxX) or (i == minY + squareLen and maxX - squareLen <= j <= maxX) or (minY <= i <= minY + squareLen and j == maxX) or (minY <= i <= minY + squareLen and j == maxX - squareLen):
        pass
    else:
        cnt += 1
        break
for i, j in dots:
    if (i == maxY and minX <= j <= minX + squareLen) or (i == maxY - squareLen and minX <= j <= minX + squareLen) or (maxY-squareLen <= i <= maxY and j == minX) or (maxY-squareLen <= i <= maxY and j == minX + squareLen):
        pass
    else:
        cnt += 1
        break
for i, j in dots:
    if (i == maxY and maxX - squareLen <= j <= maxX) or (i == maxY + squareLen and maxX - squareLen <= j <= maxX) or (maxY <= i <= maxY + squareLen and j == maxX) or (maxY <= i <= maxY + squareLen and j == maxX - squareLen):
        pass
    else:
        cnt += 1
        break

if cnt == 4:
    print(-1)
else:
    print(squareLen)