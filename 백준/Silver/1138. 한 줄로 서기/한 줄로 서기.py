num = int(input())
arr = list(map(int,input().split()))

def function(n, array):
    answer = [n+1] * n
    for i in range(n):
        cnt = 0
        goal = array[i]
        for j in range(n):
            if cnt < goal:
                if answer[j] > i + 1:
                    cnt += 1
            else:
                if answer[j] == n+1:
                    answer[j] = i + 1
                    break
                else:
                    continue
    return answer

print(*function(num, arr))