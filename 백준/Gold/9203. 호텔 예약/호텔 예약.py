import sys

common_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leaf_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1,13):
    common_year[i] += common_year[i-1]
    leaf_year[i] += leaf_year[i-1]

T = int(sys.stdin.readline())
for _ in range(T):
    arr = [0] * ((4 * 365 + 1) * 24 * 60 + 362)
    B, C = map(int,sys.stdin.readline().rstrip("\n").split())
    minima = ((4 * 365 + 1) * 24 * 60 + 362)
    maxima = 0
    for _ in range(B):
        book = list(sys.stdin.readline().rstrip("\n").split())
        start, end = [book[1], book[2]], [book[3], book[4]]
        start_date = list(map(int,start[0].split("-")))
        start_time = list(map(int,start[1].split(":")))
        end_date = list(map(int, end[0].split("-")))
        end_time = list(map(int, end[1].split(":")))
        if start_date[0] != 2016:
            start_idx = (start_date[0] - 2013) * 365 * 24 * 60 + (common_year[start_date[1] - 1] + start_date[2] - 1) * 24 * 60 + (start_time[0] * 60) + start_time[1]
        else:
            start_idx = (start_date[0] - 2013) * 365 * 24 * 60 + (leaf_year[start_date[1] - 1] + start_date[2] - 1) * 24 * 60 + (start_time[0] * 60) + start_time[1]
        if end_date[0] != 2016:
            end_idx = (end_date[0] - 2013) * 365 * 24 * 60 + (common_year[end_date[1] - 1] + end_date[2] - 1) * 24 * 60 + (end_time[0] * 60) + end_time[1] + C
        else:
            end_idx = (end_date[0] - 2013) * 365 * 24 * 60 + (leaf_year[end_date[1] - 1] + end_date[2] - 1) * 24 * 60 + (end_time[0] * 60) + end_time[1] + C
        # print("ticket : ", book[0])
        # print(start_idx)
        # print(end_idx)
        arr[start_idx] += 1
        arr[end_idx] -= 1
        if start_idx < minima:
            minima = start_idx
        if start_idx > maxima:
            maxima = start_idx + 1
    answer = 0
    value = 0
    for i in range(minima, maxima + 1):
        if arr[i]:
            value += arr[i]
            answer = max(answer, value)
    print(answer)

