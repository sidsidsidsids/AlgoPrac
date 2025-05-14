N = int(input())
S = input()
value = 0
bonus = 0
for n in range(N):
    K = S[n]
    if K == "O":
        value += (n+1) + bonus
        bonus += 1
    else:
        bonus = 0
print(value)
