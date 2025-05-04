N = int(input())
S = input()

숫자 = False
소문 = False
대문 = False
특문 = False

for s in S:
    if not s.isalnum():
        특문 = True
    elif s.isalpha():
        if s.isupper():
            대문 = True
        elif s.islower():
            소문 = True
    elif s.isdigit():
        숫자 = True

print(max(6 - len(S), 4 - sum([숫자, 소문, 대문, 특문])))