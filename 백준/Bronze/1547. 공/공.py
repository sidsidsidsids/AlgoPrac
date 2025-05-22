cups = [0,1,0,0]
for _ in range(int(input())):
    X, Y = map(int, input().split())
    cups[X], cups[Y] = cups[Y], cups[X]
for i in range(1,4):
    if cups[i]:
        print(i)
        break
