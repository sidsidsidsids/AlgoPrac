n = int(input())

def twoLiquid(liquids):
    L = len(liquids)
    liquids = sorted(liquids)
    checker = 2000000001
    s = 0
    e = L-1
    while s < e:
        test = liquids[s] + liquids[e]
        if test == 0:
            ans = [liquids[s], liquids[e]]
            break
        else:
            if abs(test) < checker:
                checker = abs(test)
                ans = [liquids[s], liquids[e]]
            if test > 0:
                e -= 1
            else:
                s += 1
    return ans

answer = twoLiquid(list(map(int,input().split())))
print(*answer)