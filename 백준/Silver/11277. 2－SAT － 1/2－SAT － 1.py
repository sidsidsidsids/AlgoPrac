import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
F = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(M)]

U = 2 ** N
flag = False
for u in range(U):
    able = True
    for m in range(M):
        i, j = F[m]
        case_flag = False
        if i > 0:
            if (u & (1 << (i - 1))):
                case_flag = True
        else:
            if not (u & (1 << (-i - 1))):
                case_flag = True

        if j > 0:
            if (u & (1 << (j - 1))):
                case_flag = True
        else:
            if not (u & (1 << (-j - 1))):
                case_flag = True

        if not case_flag:
            able = False
            break

    if able:
        flag = True
        break

print(1 if flag else 0)