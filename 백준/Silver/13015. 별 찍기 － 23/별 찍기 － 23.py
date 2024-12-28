N = int(input())
arr = []
volume = N - 2
center = (N - 1) * 2 - 1
start_tab = 1
arr.append('*' * N + ' ' * center + '*' * N)
center -= 2
while center > 0:
    arr.append(' ' * start_tab + '*' + ' ' * volume + '*' + ' ' * center + \
               '*' + ' ' * volume + '*')
    start_tab += 1
    center -= 2
arr.append(' ' * start_tab + '*' + ' ' * volume + '*' + ' ' * volume + '*')

for n in range(N):
    print(arr[n])
for n in range(N-2, -1, -1):
    print(arr[n])