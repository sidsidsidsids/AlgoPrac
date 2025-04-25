for _ in range(int(input())):
    S = list(input().split())
    print(*S[2:], *S[:2])