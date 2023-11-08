n, m = map(int,input().split())
if n // 2 < m:
    m = n-m
t = m
top = 1
bot = 1
for i in range(t):
    top *= n
    bot *= m
    n -= 1
    m -= 1
print(top//bot)