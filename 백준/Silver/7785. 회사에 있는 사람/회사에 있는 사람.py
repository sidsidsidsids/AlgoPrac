N = int(input())
S = set()
for _ in range(N):
    name, info = input().split()
    if info == "enter":
        S.add(name)
    elif info == "leave":
        S.remove(name)
S = sorted(list(S), reverse=True)
for s in S:
    print(s)