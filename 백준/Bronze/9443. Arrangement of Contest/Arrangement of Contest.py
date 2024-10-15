import sys

N = int(sys.stdin.readline().rstrip('\n'))
D = dict()
for _ in range(N):
    S = sys.stdin.readline().rstrip('\n')
    D[ord(S[0])] = True

answer = 0
for n in range(65, 91):
    if n in D:
        answer += 1
    else:
        break

print(answer)