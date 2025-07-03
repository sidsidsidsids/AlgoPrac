H, M, S = map(int, input().split())
D = int(input())
seconds = H * 3600 + M * 60 + S + D
H = (seconds // 3600) % 24
M = (seconds % 3600) // 60
S = seconds % 60
print(H, M, S)