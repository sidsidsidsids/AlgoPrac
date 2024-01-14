import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())

target = [0] * K
for k in range(K):
    y, x = map(int,input().split())
    target[k] = (y, x)

target = sorted(target, key=lambda X:(X[1], X[0]))
done = [0] * K
cnt = 0
for idx in range(K):
    if not done[idx]:
        cnt += 1
        done[idx] = 1
        tidx = idx
        while True:
            y, x = target[tidx][0], target[tidx][1]
            change = False
            for nidx in range(tidx + 1, K):
                if not done[nidx]:
                    if y <= target[nidx][0] and x <= target[nidx][1]:
                        tidx = nidx
                        done[nidx] = 1
                        change = True
                        break
            if not change:
                break
print(cnt)
