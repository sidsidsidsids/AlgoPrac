N, M, K = map(int,input().split())
beers = [[] * K for _ in range(K)]
for k in range(K):
    v, u = map(int,input().split())
    beers[k] = [v, u]

beers = sorted(beers, key=lambda X:X[1])
s = 0
e = beers[-1][1]
ans = -1
while s <= e:
    mid = (s + e) // 2
    like = 0
    ableDrink = []
    for beer in beers:
        if beer[1] <= mid:
            ableDrink.append(beer[0])
        else:
            break
    if len(ableDrink) >= N:
        sortArr = sorted(ableDrink)
        like = sum(sortArr[-N:])
    else:
        pass
    if like >= M:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)