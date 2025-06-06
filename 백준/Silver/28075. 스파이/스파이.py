N, M = map(int, input().split())
정보수집 = list(map(int, input().split()))
감시 = list(map(int, input().split()))
answer = 0
def 재귀(depth, before, score):
    global answer
    if depth == N:
        if score >= M:
            answer += 1
        return
    for i in range(3):
        v1 = 정보수집[i]
        v2 = 감시[i]
        if i == before:
            v1 /= 2
            v2 /= 2
        재귀(depth + 1, i, score + v1)
        재귀(depth + 1, i, score + v2)
재귀(0, -1, 0)
print(answer)