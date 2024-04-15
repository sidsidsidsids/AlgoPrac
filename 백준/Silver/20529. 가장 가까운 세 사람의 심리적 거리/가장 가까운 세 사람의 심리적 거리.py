import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    mbti = list(input().rstrip("\n").split())

    if N > 32:
        print(0)
        continue

    answer = 4 * N
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                temp = 0
                for x in range(4):
                    if mbti[i][x] != mbti[j][x]:
                        temp += 1
                    if mbti[i][x] != mbti[k][x]:
                        temp += 1
                    if mbti[j][x] != mbti[k][x]:
                        temp += 1
                if answer > temp:
                    answer = temp
    print(answer)
