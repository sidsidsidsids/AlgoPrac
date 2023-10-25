cows = input()
cnt = 0
check = []
for i in range(52):
    if cows[i] not in check:
        check.append(cows[i])
        nidx = 0
        flict = []
        while True:
            nidx += 1
            if i+nidx < 52:
                if cows[i] != cows[i+nidx]:
                    if cows[i+nidx] not in flict and cows[i+nidx] not in check:
                        flict.append(cows[i+nidx])
                    else:
                        if cows[i+nidx] in flict:
                            flict.remove(cows[i+nidx])
                else:
                    if flict:
                        cnt += len(flict)
                        break
            else:
                if flict:
                    cnt += len(flict)
                break
print(cnt)