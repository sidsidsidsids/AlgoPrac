J = list(map(int,input().split()))
S = list(map(int,input().split()))
jScore = 0
sScore = 0
win = False
for i in range(9):
    jScore += J[i]
    if jScore > sScore:
        win = True
        break
    sScore += S[i]

if win:
    print("Yes")
else:
    print("No")