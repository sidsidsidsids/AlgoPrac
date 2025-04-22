S = list(input().split())
UCPC = 0
for E in S:
    for s in E:
        if s.isupper():
            if s == "U" and UCPC == 0:
                UCPC += 1
            elif s == "C":
                if UCPC in [1, 3]:
                    UCPC += 1
            elif s == "P" and UCPC == 2:
                UCPC += 1
        if UCPC == 4:
            break
print("I love UCPC" if UCPC == 4 else "I hate UCPC")