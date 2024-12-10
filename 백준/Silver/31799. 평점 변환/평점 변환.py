grade = {'A', 'B', 'C'}
symbol = {'0', '+', '-'}
N = int(input())
S = input()

tmp = ''
graded = False
lst = []
for s in S:
    if not graded:
        tmp += s
        graded = True
        continue
    if s in symbol:
        tmp += s
        lst.append(tmp)
        tmp = ''
        graded = False
        continue
    else:
        lst.append(tmp + '0')
        tmp = s
        continue
if tmp:
    lst.append(tmp + '0')

answer = ''
for n in range(N):
    grade = lst[n]
    if grade == 'C+' or grade == 'C0' or grade == 'C-':
        answer += 'B'
    elif grade == 'B0' or grade == 'B-':
        if n == 0 or (lst[n-1] == 'C+' or lst[n-1] == 'C0' or lst[n-1] == 'C-'):
            answer += 'D'
        else:
            answer += 'B'
    elif grade == 'A-' or grade == 'B+':
        if n == 0 or (lst[n-1] == 'B0' or lst[n-1] == 'B-' or \
                      lst[n-1] == 'C+' or lst[n-1] == 'C0' or lst[n-1] == 'C-'):
            answer += 'P'
        else:
            answer += 'D'
    elif grade == 'A0':
        if n == 0 or (lst[n-1] == 'A-' or lst[n-1] == 'B+' or lst[n-1] == 'B0' or \
                      lst[n-1] == 'B-' or lst[n-1] == 'C+' or lst[n-1] == 'C0' or \
                      lst[n-1] == 'C-'):
            answer += 'E'
        else:
            answer += 'P'
    elif grade == 'A+':
        answer += 'E'

print(answer)
