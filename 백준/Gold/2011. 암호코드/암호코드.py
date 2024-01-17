code = str(input())
L = len(code)

ans = 0
dp = [0] * L
idx = 0
seq = False
while idx < L:
    if code[idx] == '0':
        if idx == 0 or code[idx - 1] == '0' or int(code[idx - 1]) > 2:
            break
        else:
            if idx > 1:
                dp[idx] = dp[idx - 2]
                dp[idx - 1] = dp[idx - 2]
            else:
                dp[idx] = dp[idx - 1]
    else:
        if idx == 0:
            dp[idx] = 1
        else:
            if code[idx - 1] == '0':
                seq = False
                dp[idx] = dp[idx - 1]
            elif int(code[idx - 1:idx + 1]) <= 26:
                if seq:
                    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1000000
                else:
                    seq = True
                    dp[idx] = (dp[idx - 1] * 2) % 1000000
            else:
                seq = False
                dp[idx] = dp[idx - 1]
    idx += 1
ans = dp[-1]
print(ans)