arr = [0] * 5
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
for r in range(R-1):
    for c in range(C-1):
        cars = 0
        blocked = False
        for y, x in [(r, c), (r, c+1), (r+1, c), (r+1, c+1)]:
            V = grid[y][x]
            if V == "X":
                cars += 1
            elif V == "#":
                blocked = True
                break
        if not blocked:
            arr[cars] += 1
for elem in arr:
    print(elem)