import sys

while True:
    S = sys.stdin.readline().rstrip('\n')
    if S == "halt":
        break
    before = 1
    count = 0
    for s in S:
        if s == "a":
            if before == 2:
                count += 2
            count += 1
            before = 2
        elif s == "b":
            if before == 2:
                count += 2
            count += 2
            before = 2
        elif s == "c":
            if before == 2:
                count += 2
            count += 3
            before = 2
        elif s == "d":
            if before == 3:
                count += 2
            count += 1
            before = 3
        elif s == "e":
            if before == 3:
                count += 2
            count += 2
            before = 3
        elif s == "f":
            if before == 3:
                count += 2
            count += 3
            before = 3
        elif s == "g":
            if before == 4:
                count += 2
            count += 1
            before = 4
        elif s == "h":
            if before == 4:
                count += 2
            count += 2
            before = 4
        elif s == "i":
            if before == 4:
                count += 2
            count += 3
            before = 4
        elif s == "j":
            if before == 5:
                count += 2
            count += 1
            before = 5
        elif s == "k":
            if before == 5:
                count += 2
            count += 2
            before = 5
        elif s == "l":
            if before == 5:
                count += 2
            count += 3
            before = 5
        elif s == "m":
            if before == 6:
                count += 2
            count += 1
            before = 6
        elif s == "n":
            if before == 6:
                count += 2
            count += 2
            before = 6
        elif s == "o":
            if before == 6:
                count += 2
            count += 3
            before = 6
        elif s == "p":
            if before == 7:
                count += 2
            count += 1
            before = 7
        elif s == "q":
            if before == 7:
                count += 2
            count += 2
            before = 7
        elif s == "r":
            if before == 7:
                count += 2
            count += 3
            before = 7
        elif s == "s":
            if before == 7:
                count += 2
            count += 4
            before = 7
        elif s == "t":
            if before == 8:
                count += 2
            count += 1
            before = 8
        elif s == "u":
            if before == 8:
                count += 2
            count += 2
            before = 8
        elif s == "v":
            if before == 8:
                count += 2
            count += 3
            before = 8
        elif s == "w":
            if before == 9:
                count += 2
            count += 1
            before = 9
        elif s == "x":
            if before == 9:
                count += 2
            count += 2
            before = 9
        elif s == "y":
            if before == 9:
                count += 2
            count += 3
            before = 9
        elif s == "z":
            if before == 9:
                count += 2
            count += 4
            before = 9
    print(count)