import sys

answers = []
while True:
    n, o, w = sys.stdin.readline().split()
    if n == "#" and o == "0" and w == "0":
        break
    c = "Junior"
    if int(o) > 17 or int(w) >= 80:
        c = "Senior"
    answers.append([n, c])
for answer in answers:
    print(*answer)