N = int(input())
T = list(map(int, input().split()))
T = sorted(T)
answer = list
value = 3000000001
for i in range(1, N-1):
    if value == 0:
        break
    l = 0
    r = N - 1
    I = T[i]
    while l < i and i < r:
        tmp_val = T[l] + I + T[r]
        if abs(tmp_val) < value:
            value = abs(tmp_val)
            answer = [T[l], I, T[r]]
        if tmp_val == 0:
            break
        if tmp_val < 0:
            l += 1
        else:
            r -= 1
print(*answer)