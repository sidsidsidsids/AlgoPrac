import sys
N = int(sys.stdin.readline())
info = dict()
cnt = 0
maxima = -1
answer = ''
arr = [0] * (10000 * 12 + 1)
for _ in range(N):
    start, end = sys.stdin.readline().rstrip("\n").split()
    s_year, s_month = map(int,start.split("-"))
    arr[s_year * 12 + s_month - 1] += 1
    e_year, e_month = map(int,end.split("-"))
    arr[e_year * 12 + e_month] -= 1

for time in range(len(arr)):
    if arr[time]:
        cnt += arr[time]
        if cnt > maxima:
            maxima = cnt
            year = time // 12
            month = time % 12 + 1
            if month >= 10:
                answer = str(year) + '-' + str(month)
            else:
                answer = str(year) + '-0' + str(month)

print(answer)
