import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
    if a == 0 and b == 0 and c == 0:
        break
    if a < b + c and b < a + c and c < a + b:
        if a == b and b == c and a == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        elif a != b and b != c and a != c:
            print("Scalene")
    else:
        print("Invalid")