N, K = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

def function(coins, goal):
    answer = 0
    cases = [0] * (goal + 1)
    cases[0] = 1
    for coin in coins:
        for i in range(goal + 1):
            if i - coin >= 0:
                cases[i] += cases[i - coin]
    answer = cases[goal]
    return answer

print(function(arr, K))