import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    result = list()
    target = set()

    for n in range(N):
        a, b = map(int,input().split())
        result.append((a,b))

    result = sorted(result, key=lambda x:x[0])
    ans = 1
    bVal = result[0][1]

    for n in range(1,N):
        if result[n][1] < bVal:
            ans += 1
            bVal = result[n][1]

    print(ans)



