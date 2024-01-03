N, L = map(int,input().split())
spots = [() for _ in range(N)]
for n in range(N):
    s, e = map(int,input().split())
    spots[n] = (s, e)
spots = sorted(spots)

cur_loc = spots[0][0]
cnt = 0
for s, e in spots:
    if cur_loc > e:
        continue
    elif cur_loc < s:
        cur_loc = s
    dist = e - cur_loc
    if not dist % L:
        r = 0
    else:
        r = 1
    check = dist // L + r
    cnt += check
    cur_loc += L * check
print(cnt)