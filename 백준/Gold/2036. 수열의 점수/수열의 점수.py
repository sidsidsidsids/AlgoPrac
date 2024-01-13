import sys
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
score = 0
zero_cnt = False

for n in range(N):
    elem = int(input())
    if elem > 0:
        plus.append(elem)
    elif elem < 0:
        minus.append(elem)
    else:
        zero_cnt += True

plus = sorted(plus)
minus = sorted(minus, reverse=True)
while plus:
    if len(plus) > 1:
        elem1 = plus.pop()
        elem2 = plus.pop()
        if elem1 == 1 or elem2 == 1:
            score += elem1 + elem2
        else:
            score += elem1 * elem2
    elif len(plus) == 1:
        elem1 = plus.pop()
        score += elem1
        break
    else:
        break

while minus:
    if len(minus) > 1:
        elem1 = minus.pop()
        elem2 = minus.pop()
        score += elem1 * elem2
    elif len(minus) == 1:
        elem1 = minus.pop()
        if zero_cnt:
            pass
        else:
            score += elem1
        break
    else:
        break
print(score)