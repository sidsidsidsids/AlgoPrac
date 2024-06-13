import sys

T = int(sys.stdin.readline().rstrip('\n'))
answer = []
for _ in range(T):
    P = sys.stdin.readline().rstrip('\n')
    L = len(P)
    able = False
    Q = [0]
    V = [0] * (L+1)
    V[0] = 1
    while Q:
        if V[L]:
            able = True
            break
        i = Q.pop()
        if i + 2 <= L and P[i] == '0' and P[i+1] == '1':
            if not V[i+2]:
                Q.append(i+2)
                V[i+2] = 1
        if i + 4 <= L and P[i] == '1' and (P[i+1] == P[i+2] == '0'):
            k = 3
            flag = True
            while i + k < L:
                if flag:
                    if P[i + k] == '0':
                        k += 1
                    else:
                        flag = False
                        if not V[i+k + 1]:
                            Q.append(i+k + 1)
                            V[i+k + 1] = 1
                else:
                    if P[i + k] == '0':
                        break
                    else:
                        if not V[i+k + 1]:
                            Q.append(i+k + 1)
                            V[i+k + 1] = 1
                        k += 1
    answer.append('YES' if able else 'NO')

for ans in answer:
    print(ans)