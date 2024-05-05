n = int(input())
m = int(input())
s = input()

target = 'I' + ('OI'*n)
len_t = len(target)
len_s = len(s)

table = [0] * len_t
pidx = 0
for idx in range(1, len_t):
    while pidx and target[pidx] != target[idx]:
        pidx = table[pidx - 1]

    if target[idx] == target[pidx]:
        pidx += 1
        table[idx] = pidx

answer = 0
pidx = 0

for idx in range(len_s):
    while pidx > 0 and s[idx] != target[pidx]:
        pidx = table[pidx - 1]

    if s[idx] == target[pidx]:
        if pidx == len_t - 1:
            answer += 1
            pidx = table[pidx]
        else:
            pidx += 1

print(answer)