import sys

G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())

plane_rec = [g for g in range(G+1)]
gate_rec = [0] * (G+1)
answer = 0

flag = True
for _ in range(P):
    D = int(sys.stdin.readline().strip())
    if not flag:
        continue
    for d in range(plane_rec[D], 0, -1):
        if not gate_rec[d]:
            gate_rec[d] = 1
            plane_rec[D] = d
            answer += 1
            break
    else:
        flag = False

print(answer)