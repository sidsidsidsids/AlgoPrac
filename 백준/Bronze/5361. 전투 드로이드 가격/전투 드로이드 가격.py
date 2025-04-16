N = int(input())

A = 35034
B = 23090
C = 19055
D = 12530
E = 18090
for _ in range(N):
    a, b, c, d, e = map(int, input().split())
    price = (A*a + B*b + C*c + D*d + E*e) / 100
    print(f"${price:.2f}")