N = int(input())
fibo =[[] for _ in range(41)]
fibo[0] = [1,0]
fibo[1] = [0,1]

for t in range(2,41):
    fibo[t] = [fibo[t-2][0] + fibo[t-1][0], fibo[t-2][1] + fibo[t-1][1]]

for n in range(N):
    i = int(input())
    print(*fibo[i])