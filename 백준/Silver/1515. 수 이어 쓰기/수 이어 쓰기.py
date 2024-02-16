N = input()
len_N = len(N)
i = 0
ans = 0
while i < len_N:
    ans += 1
    for val in str(ans):
        if val == N[i]:
            i += 1
            if i == len_N:
                break
print(ans)