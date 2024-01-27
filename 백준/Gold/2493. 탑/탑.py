N = int(input())
arr = list(map(int,input().split()))
answers = [0] * N
stack = []
for i in range(N-1,0,-1):
    if arr[i] <= arr[i-1]:
        answers[i] = i
        if stack:
            while True:
                if stack and stack[-1][0] <= arr[i-1]:
                    elem = stack.pop()
                    answers[elem[1]] = i
                else:
                    break
    else:
        stack.append([arr[i], i])
for answer in answers:
    print(answer, end=" ")