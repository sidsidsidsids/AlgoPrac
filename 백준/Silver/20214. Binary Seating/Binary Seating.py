import sys

N = int(sys.stdin.readline().rstrip('\n'))
T = list(map(int, sys.stdin.readline().rstrip('\n').split()))

T.sort(reverse=True)
value = 0.5
answer = 0
for elem in T:
    answer += elem * value
    value /= 2
print(round(answer, 6))