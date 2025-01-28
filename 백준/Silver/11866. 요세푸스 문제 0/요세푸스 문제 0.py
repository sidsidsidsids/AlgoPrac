import sys

N, K = map(int, sys.stdin.readline().strip().split())
arr = [n for n in range(1, N+1)]
visit = [0] * N
L = 0
i = -1
k = K
answer = ""
while L < N:
    i += 1
    if i >= N:
        i = 0
    if visit[i]:
        continue
    else:
        k -= 1
        if k == 0:
            if answer:
                answer += ", "
            answer += str(arr[i])
            visit[i] = 1
            L += 1
            k = K

print("<" + answer + ">")