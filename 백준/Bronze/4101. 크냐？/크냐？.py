while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print("Yes" if a > b else "No")