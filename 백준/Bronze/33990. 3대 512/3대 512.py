answer = 601
for _ in range(int(input())):
    S = sum(list(map(int, input().split())))
    if S >= 512:
        answer = min(answer, S)
print(answer if answer != 601 else -1)