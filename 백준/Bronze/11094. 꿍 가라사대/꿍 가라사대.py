N = int(input())
for _ in range(N):
    S = input()
    if S.startswith("Simon says"):
        T = S.replace("Simon says","")
        print(T)