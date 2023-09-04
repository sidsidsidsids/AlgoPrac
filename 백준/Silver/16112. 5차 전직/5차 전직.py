n, k = map(int,input().split())
questExp = list(map(int,input().split()))
questExp = sorted(questExp, reverse=False)

value = 0
active = 0

for exp in questExp:
    value += exp * active
    if active < k:
        active += 1

print(value)