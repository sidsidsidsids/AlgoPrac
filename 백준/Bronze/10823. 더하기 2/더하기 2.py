S = ''
while True:
    try:
        S += input().strip()
    except:
        break
S = sum(map(int, S.split(",")))
print(S)