N = int(input())
i = 1
a = 1
while True:
    if N >= int("1" * i):
        a = i
        i += 1
        continue
    else:
        break
print(a)