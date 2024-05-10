N = int(input())
profit = list(map(int,input().split()))
price = list(map(int,input().split()))
sorted_profit = sorted(profit, reverse=True)
maxone = sorted_profit[0]
maxtwo = sorted_profit[1]
answer = [0] * N
for n in range(N):
    if profit[n] == maxone:
        answer[n] = profit[n] - maxtwo
    else:
        answer[n] = profit[n] - maxone
print(*answer)