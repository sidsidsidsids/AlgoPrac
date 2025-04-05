import sys


def check(targets: list):
    flag = True
    for i in range(4):
        if ord(targets[i+1]) in [ord(targets[i]) + 1, ord(targets[i]) - 1]:
            continue
        else:
            flag = False
            break
    return flag


N = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
for n in range(N-4):
    K = S[n:n+5]
    if check(K):
        print("YES")
        break
else:
    print("NO")