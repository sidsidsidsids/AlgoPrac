from collections import deque
N, Q = map(int,input().split())
backStack = deque()
forStack = deque()
compress = deque()
curPage = 0
for q in range(Q):
    work = input().split()
    if len(work) == 1:
        if work[0] == 'B':
            if backStack:
                if curPage:
                    forStack.append(curPage)
                nextPage = backStack.pop()
                curPage = nextPage
        elif work[0] == 'F':
            if forStack:
                if curPage:
                    backStack.append(curPage)
                nextPage = forStack.pop()
                curPage = nextPage
        elif work[0] == 'C':
            if backStack:
                size = len(backStack)
                for idx in range(size):
                    if compress:
                        if compress[-1] != backStack[idx]:
                            compress.append(backStack[idx])
                    else:
                        compress.append(backStack[idx])
                backStack = compress
                compress = deque()
    else:
        if curPage:
            backStack.append(curPage)
        curPage = work[1]
        forStack = deque()
    # print(f'{q+1}번째 동작: {work[0]} ',"현재: ", curPage, "뒤로가기스택: ", backStack, "앞으로스택: ", forStack)

print(curPage)
if backStack:
    size = len(backStack)
    for idx in range(size-1,-1,-1):
        print(backStack[idx], end=" ")
    print()
else:
    print(-1)
if forStack:
    size = len(forStack)
    for idx in range(size-1,-1,-1):
        print(forStack[idx], end=" ")
    print()
else:
    print(-1)