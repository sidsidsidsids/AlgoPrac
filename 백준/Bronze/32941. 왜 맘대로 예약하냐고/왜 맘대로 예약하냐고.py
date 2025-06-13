T, X = map(int, input().split())
N = int(input())
able = True
for _ in range(N):
    K = int(input())
    A = set(map(int, input().split()))
    if X not in A:
        able = False
print("YES" if able else "NO")