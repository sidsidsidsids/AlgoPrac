N = int(input())
case = 1
while N:
    grid = []
    for _ in range(9):
        grid.append(list(map(int, input().split())))

    able = True
    printed = False
    for i in range(9):
        temp_set = set()
        for j in range(9):
            temp_set.add(grid[i][j])
        if len(temp_set) != 9:
            able = False
            break

    if not able:
        print(f"Case {case}: INCORRECT")
        printed = True
    else:
        for j in range(9):
            temp_set = set()
            for i in range(9):
                temp_set.add(grid[i][j])
            if len(temp_set) != 9:
                able = False
                break

    if not able and not printed:
        print(f"Case {case}: INCORRECT")
        printed = True
    elif able:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp_set = set()
                for y in range(3):
                    for x in range(3):
                        temp_set.add(grid[i+y][j+x])
                if len(temp_set) != 9:
                    able = False
                    break
            if not able:
                break

    if not able and not printed:
        print(f"Case {case}: INCORRECT")
    elif able:
        print(f"Case {case}: CORRECT")

    N -= 1
    case += 1
    if N:
        _ = input()