import sys

answer = 0
diff = sys.maxsize
flag = True

for _ in range(10):
    N = int(sys.stdin.readline().rstrip('\n'))
    if flag and abs(100 - (answer + N)) <= diff:
        answer += N
        diff = abs(answer - 100)
    else:
        flag = False

print(answer)