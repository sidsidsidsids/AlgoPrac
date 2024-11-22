
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a = (x1 - x2) ** 2 + (y1 - y2) ** 2
b = (x2 - x3) ** 2 + (y2 - y3) ** 2
c = (x3 - x1) ** 2 + (y3 - y1) ** 2

ccw = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

a, b, c = sorted([a, b, c])
if ccw == 0:
    print("X")
elif a == b and b == c and a == c:
    print("JungTriangle")
elif a == b or b == c or a == c:
    if a + b == c:
        print("Jikkak2Triangle")
    elif a + b < c:
        print("Dunkak2Triangle")
    elif a + b > c:
        print("Yeahkak2Triangle")
else:
    if a + b == c:
        print("JikkakTriangle")
    elif a + b < c:
        print("DunkakTriangle")
    elif a + b > c:
        print("YeahkakTriangle")