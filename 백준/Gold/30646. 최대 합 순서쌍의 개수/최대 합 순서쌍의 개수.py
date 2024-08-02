import sys

N = int(sys.stdin.readline().rstrip('\n'))
a = list(map(int, sys.stdin.readline().rstrip('\n').split()))

prefix = [0] * N
record = dict()
upper_bound = 0
upper_count = 0
for n in range(N):
    num = a[n]

    if n == 0:
        prefix[n] = num
    else:
        prefix[n] = num + prefix[n-1]

    if num in record:
        record[num][1] = n
        s = record[num][0]

        cur_bound = 0
        if s == 0:
            cur_bound = prefix[n]
        else:
            cur_bound = prefix[n] - prefix[s - 1]

        if cur_bound > upper_bound:
            upper_bound = cur_bound
            upper_count = 1
        elif cur_bound == upper_bound:
            upper_count += 1
    else:
        record[num] = [n, 0]
        if num > upper_bound:
            upper_bound = num
            upper_count = 1
        elif num == upper_bound:
            upper_count += 1

print(upper_bound, upper_count)