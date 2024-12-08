w1 = 0
w2 = 0
s1 = 0
s2 = 0

N = int(input())
arr = []
for _ in range(N):
    info = list(input().split())
    team = int(info[0])
    mm, ss = map(int, info[1].split(":"))
    arr.append((team, mm * 60 + ss))
arr = sorted(arr, key=lambda X:X[1])
i = 0
for sec in range(60 * 48):
    if i < N and sec == arr[i][1]:
        if arr[i][0] == 1:
            s1 += 1
        elif arr[i][0] == 2:
            s2 += 1
        i += 1
    if s1 != s2:
        if s1 > s2:
            w1 += 1
        elif s1 < s2:
            w2 += 1

print(f"{w1//60 if w1//60 >= 10 else '0'+str(w1//60)}:{w1%60 if w1%60 >= 10 else '0'+str(w1%60)}")
print(f"{w2//60 if w2//60 >= 10 else '0'+str(w2//60)}:{w2%60 if w2%60 >= 10 else '0'+str(w2%60)}")