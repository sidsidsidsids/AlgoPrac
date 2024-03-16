N = int(input())
arr = list(map(int,input().split()))

def func(array):
    cnt = [0] * (N + 1)
    answer = [[N, N] for _ in range(N + 1)]
    # to right
    stack = []
    for idx, val in enumerate(array, 1):
        while stack and stack[-1][1] <= val:
            stack.pop()
        cnt[idx] += len(stack)

        if stack:
            dist = abs(stack[-1][0] - idx)
            if dist < answer[idx][1]:
                answer[idx][0] = stack[-1][0]
                answer[idx][1] = dist
            elif dist == answer[idx][1] and stack[-1][0] < answer[idx][0]:
                answer[idx][0] = stack[-1][0]

        stack.append([idx, val])

    # to left
    stack = []
    for idx, val in reversed(list(enumerate(array, 1))):
        while stack and stack[-1][1] <= val:
            stack.pop()
        cnt[idx] += len(stack)

        if stack:
            dist = abs(stack[-1][0] - idx)
            if dist < answer[idx][1]:
                answer[idx][0] = stack[-1][0]
                answer[idx][1] = dist
            elif dist == answer[idx][1] and stack[-1][0] < answer[idx][0]:
                answer[idx][0] = stack[-1][0]
        stack.append([idx, val])

    # ans
    for i in range(1, N+1):
        if cnt[i]:
            print(cnt[i], answer[i][0])
        else:
            print(0)
    return

func(arr)