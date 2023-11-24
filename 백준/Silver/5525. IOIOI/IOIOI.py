n = int(input())
m = int(input())
s = input()

target = 'I' + ('OI'*n)

cnt = 0

for i in range(m-n+1):
    check = s[i:i+(n*2)+1]
    if check == target:
        cnt += 1

print(cnt)