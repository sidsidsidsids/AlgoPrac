N = int(input())
idx = -1
maxima = -1
for n in range(N):
    cards = list(map(int, input().split()))
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                value = (cards[i] + cards[j] + cards[k]) % 10
                if maxima <= value:
                    idx = n+1
                    maxima = value
print(idx)