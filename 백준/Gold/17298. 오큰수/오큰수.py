N = int(input())
arr = list(map(int,input().split()))
stack = []
answer = [-1] * N
stack.append(0)
for n in range(1, N):
    while stack and arr[stack[-1]] < arr[n]:
        answer[stack.pop()] = arr[n]
    stack.append(n)
print(*answer)