N = int(input())
sign = list(input().split())
min_ans = 10**(N+1)
max_ans = 0
def finding(idx, curNums, curElem):
    if idx == 0:
        for n in range(10):
            nums = str(n)
            curElem[n] = 1
            finding(1, nums, curElem)
            curElem[n] = 0
    elif idx == N+1:
        global min_ans
        global max_ans
        value = int(curNums)
        if value > int(max_ans):
            max_ans = curNums
        if value < int(min_ans):
            min_ans = curNums
        return
    else:
        for i in range(10):
            if not curElem[i]:
                if sign[idx-1] == '<':
                    if int(curNums[-1]) < i:
                        curElem[i] = 1
                        finding(idx + 1, curNums + str(i), curElem)
                        curElem[i] = 0
                elif sign[idx-1] == '>':
                    if int(curNums[-1]) > i:
                        curElem[i] = 1
                        finding(idx + 1, curNums + str(i), curElem)
                        curElem[i] = 0

finding(0,'',[0]*(10))
print(max_ans)
print(min_ans)