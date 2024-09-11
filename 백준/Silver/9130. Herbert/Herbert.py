import sys

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    num = int(sys.stdin.readline().rstrip('\n'))
    if num < 2:
        if num == 1:
            print(2)
        else:
            print(1)
    else:
        print(2*num*num - 4*num + 5)