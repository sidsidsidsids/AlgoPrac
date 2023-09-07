R, C = map(int,input().split())
farm = [list(input()) for _ in range(R)]

able = True
for r in range(R):
    for c in range(C):
        if farm[r][c] == "W":
            for nr, nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0 <= nr < R and 0 <= nc < C:
                    if farm[nr][nc] == "S":
                        able = False
                        break
        if not able:
            break
    if not able:
        break

if not able:
    print(0)
else:
    print(1)
    for r in range(R):
        for c in range(C):
            if farm[r][c] == ".":
                print("D", end="")
            else:
                print(farm[r][c], end="")
        print()