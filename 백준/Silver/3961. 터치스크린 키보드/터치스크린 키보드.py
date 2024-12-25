from collections import deque, defaultdict
import sys
keyboard = [list('qwertyuiop'),list('asdfghjkl'),list('zxcvbnm')]
info = defaultdict(dict)
for y in range(3):
    for x in range(10 - y):
        if y == 2 and x == 7:
            break
        A = keyboard[y][x]
        info[A][A] = 0
        Q = deque()
        Q.append((y, x))
        V = set()
        V.add(A)
        dist = 1
        L = 1
        while Q:
            i, j = Q.popleft()
            L -= 1
            for ny, nx in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if ny == 0:
                    if 0 <= nx <= 9 and keyboard[ny][nx] not in V:
                        info[A][keyboard[ny][nx]] = dist
                        V.add(keyboard[ny][nx])
                        Q.append((ny, nx))
                elif ny == 1:
                    if 0 <= nx <= 8 and keyboard[ny][nx] not in V:
                        info[A][keyboard[ny][nx]] = dist
                        V.add(keyboard[ny][nx])
                        Q.append((ny, nx))
                elif ny == 2:
                    if 0 <= nx <= 6 and keyboard[ny][nx] not in V:
                        info[A][keyboard[ny][nx]] = dist
                        V.add(keyboard[ny][nx])
                        Q.append((ny, nx))
            if L == 0:
                L = len(Q)
                dist += 1

answers = []
T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    word, nums = sys.stdin.readline().rstrip('\n').split()
    w_l = len(word)
    checks = []
    for _ in range(int(nums)):
        wordle = sys.stdin.readline().rstrip('\n')
        value = 0
        for l in range(w_l):
            value += info[word[l]][wordle[l]]
        checks.append([wordle, value])
    checks = sorted(checks, key=lambda X:(X[1], X[0]))
    answers.append(checks)
for result in answers:
    for elem in result:
        print(*elem)