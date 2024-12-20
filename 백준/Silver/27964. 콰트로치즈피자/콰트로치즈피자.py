N = int(input())
T = list(input().split())

C = set()
cnt = 0
for e in T:
    if cnt >= 4:
        break
    if e[-6:] == "Cheese" and e not in C:
        C.add(e)
        cnt += 1
print("yummy" if cnt >= 4 else "sad")