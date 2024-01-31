first = input()
second = input()
third = input()
f_len = len(first) + 1
s_len = len(second) + 1
t_len = len(third) + 1
dp = [[[0] * t_len for _ in range(s_len)] for _ in range(f_len)]
for i in range(1, f_len):
    for j in range(1, s_len):
        for k in range(1, t_len):
            if first[i-1] == second[j-1] == third[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])