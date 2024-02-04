N, D, K, C = map(int,input().split())
# 접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수, 쿠폰 번호
arr = [0] * N
for n in range(N):
    arr[n] = int(input())

ans = 0
s = 0
e = K - 1
record = [0] * (D + 1)
i = s
while i <= e:
    record[arr[i]] += 1
    if record[arr[i]] == 1:
        ans += 1
    i += 1
cnt = ans
if not record[C]:
    ans += 1

s += 1
e += 1
if e == N:
    e = 0
while s != 0:
    record[arr[s-1]] -= 1
    if record[arr[s-1]] == 0:
        cnt -= 1
    record[arr[e]] += 1
    if record[arr[e]] == 1:
        cnt += 1

    if record[C]:
        if cnt > ans:
            ans = cnt
    else:
        if cnt + 1 > ans:
            ans = cnt + 1

    s += 1
    e += 1
    if s == N:
        s = 0
    if e == N:
        e = 0

print(ans)