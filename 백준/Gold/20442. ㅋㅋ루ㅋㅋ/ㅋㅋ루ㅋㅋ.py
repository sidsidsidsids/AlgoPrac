kkrkk = input()
L = len(kkrkk)
Q = []
for idx in range(L):
    if kkrkk[idx] == 'R':
        Q.append(idx)
LQ = len(Q)
if not Q:
    print(0)
elif LQ == 1:
    l = Q[0]
    print(1 + min(l, L-(l+1)) * 2)
else:
    init_value = LQ
    answer = 0
    answer += init_value
    l_idx = 0
    r_idx = init_value - 1
    l = Q[l_idx]
    r = Q[r_idx]
    l_c = 0
    r_c = 0
    while l_idx <= r_idx:
        if l != 0 and r != L-1:
            value = init_value + min(l - l_c, L-(r+1) - r_c) * 2
        elif l == 0 or r == L-1:
            value = init_value
        if value > answer:
            answer = value
        if l-l_c > L-(r+1)-r_c:
            r_idx -= 1
            r = Q[r_idx]
            r_c += 1
            if init_value > 1:
                init_value -= 1
        else:
            l_idx += 1
            if l_idx >= LQ:
                break
            l = Q[l_idx]
            l_c += 1
            if init_value > 1:
                init_value -= 1
    print(answer)



