import sys
import heapq

N = int(sys.stdin.readline().rstrip('\n'))
V = [0] * N
OG = [0] * N
HQ = [0] * N
for n in range(N):
    v = int(sys.stdin.readline().rstrip('\n'))
    OG[n] = v
    HQ[n] = (-v, n)
heapq.heapify(HQ)
answer = []
while HQ:
    val, idx = heapq.heappop(HQ)
    if V[idx] == 1:
        pass
    else:
        V[idx] = 1
        answer.append(idx + 1)
        l_val = -val
        for l in range(idx - 1, -1, -1):
            nv = OG[l]
            if l_val > nv:
                l_val = nv
                V[l] = 1
                continue
            else:
                break
        r_val = -val
        for r in range(idx + 1, N):
            nv = OG[r]
            if r_val > nv:
                r_val = nv
                V[r] = 1
                continue
            else:
                break
answer.sort()
for e in answer:
    print(e)