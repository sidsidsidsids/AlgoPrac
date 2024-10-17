import sys

while True:
    N = int(sys.stdin.readline().rstrip('\n'))
    if N == 0:
        break
    shelf = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    money = 0
    for n in range(N):
        price = shelf[n]
        if money + price <= 300:
            money += price
    print(money)