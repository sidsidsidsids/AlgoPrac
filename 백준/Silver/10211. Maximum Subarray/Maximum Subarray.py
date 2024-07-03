import sys
T = int(sys.stdin.readline().rstrip('\n'))
answer = []
for _ in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    arr = list(map(int,sys.stdin.readline().rstrip('\n').split()))

    sum_arr = [0] * N
    sum_arr[0] = arr[0]
    for n in range(1, N):
        sum_arr[n] = sum_arr[n-1] + arr[n]
    sub_sum = sum_arr[:]
    for n in range(N):
        const = sum_arr[n]
        for i in range(n):
            sub_sum[n] = max(sub_sum[n], const - sum_arr[i])
    answer.append(max(sub_sum))

for ans in answer:
    print(ans)