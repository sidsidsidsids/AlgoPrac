width, height = map(int,input().split())
x, y = map(int,input().split())
time = int(input())
if time > width*2:
    wCheck = time % (width*2)
else:
    wCheck = time
xAdj = 1
for w in range(wCheck):
    if 0 <= x <= width:
        x += xAdj
        if x == width or x == 0:
            xAdj = -xAdj
if time > height*2:
    hCheck = time % (height*2)
else:
    hCheck = time
yAdj = 1
for h in range(hCheck):
    if 0 <= y <= height:
        y += yAdj
        if y == height or y == 0:
            yAdj = -yAdj
print(x, y)