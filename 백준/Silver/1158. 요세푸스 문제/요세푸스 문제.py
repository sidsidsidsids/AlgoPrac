from collections import deque
N, K = map(int, input().rstrip('\n').split())
arr = deque()
for n in range(1, N+1):
    arr.append(n)
k = K
answer = []
while arr:
    k -= 1
    if k == 0:
        answer.append(arr.popleft())
        k = K
    else:
        arr.append(arr.popleft())
print('<',end='')
for n in range(N):
    print(answer[n],end='')
    if n != N-1:
        print(', ',end='')
print('>')