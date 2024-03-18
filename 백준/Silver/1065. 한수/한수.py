N = int(input())

def function(num):
    answer = 0
    for n in range(1, num+1):
        target = str(n)
        if len(target) < 3:
            answer += 1
        else:
            diff = False
            flag = True
            for i in range(1, len(target)):
                if i == 1:
                    diff = int(target[i-1]) - int(target[i])
                else:
                    if diff != int(target[i-1]) - int(target[i]):
                        flag = False
                        break
            if flag:
                answer += 1
    return answer

print(function(N))