import sys

HH, MM = map(int,sys.stdin.readline().rstrip('\n').split(":"))
place = list(map(int,sys.stdin.readline().rstrip('\n').split()))
L = int(sys.stdin.readline().rstrip('\n'))
for _ in range(L):
    t, command = sys.stdin.readline().rstrip('\n').split()
    time = HH * 60 + MM
    area = time // 120
    if command == '^':
        if place[area]:
            place[area] = 0
    elif command[2] == "M":
        earn = int(command[:2])
        MM += earn
        if MM >= 60:
            HH += 1
            MM -= 60
        if HH >= 12:
            HH = HH % 12
    else:
        earn = int(command[0])
        HH += earn
        if HH >= 12:
            HH = HH % 12
answer = 0
for elem in place:
    answer += elem
print(min(answer, 100))
