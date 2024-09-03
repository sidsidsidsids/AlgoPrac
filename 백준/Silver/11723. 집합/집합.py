import sys

N = int(sys.stdin.readline().rstrip('\n'))
S = set()
for _ in range(N):
    act = list(sys.stdin.readline().rstrip('\n').split())
    if act[0] == "add":
        S.add(act[1])
    elif act[0] == "remove":
        e = act[1]
        if e in S:
            S.remove(e)
    elif act[0] == "check":
        e = act[1]
        if e in S:
            print(1)
        else:
            print(0)
    elif act[0] == "toggle":
        e = act[1]
        if e in S:
            S.remove(e)
        else:
            S.add(e)
    elif act[0] == "all":
        S = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"}
    elif act[0] == "empty":
        S = set()