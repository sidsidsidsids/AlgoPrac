import sys

scenario = 1
while True:
    o, w = map(int, sys.stdin.readline().strip().split())
    if not o and not w:
        break
    while True:
        m, n = sys.stdin.readline().strip().split()
        if m == "#" and n == "0":
            break
        if m == "E":
            w -= int(n)
            if w <= 0:
                break
        elif m == "F":
            w += int(n)
    while m != "#":
        m, n = sys.stdin.readline().strip().split()
    if o / 2 < w < o * 2:
        print(scenario, ":-)")
    elif w <= 0:
        print(scenario, "RIP")
    else:
        print(scenario, ":-(")
    scenario += 1