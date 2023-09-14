N = int(input())
RGB = [[] for _ in range(N)]
for n in range(N):
    RGB[n] = list(map(int,input().split()))

for idx in range(1,N):
    RGB[idx][0] = RGB[idx][0] + min(RGB[idx-1][1], RGB[idx-1][2])
    RGB[idx][1] = RGB[idx][1] + min(RGB[idx - 1][0], RGB[idx - 1][2])
    RGB[idx][2] = RGB[idx][2] + min(RGB[idx - 1][0], RGB[idx - 1][1])

answer = min(RGB[N-1])
print(answer)