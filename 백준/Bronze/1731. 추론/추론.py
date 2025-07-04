N = int(input())
S = [int(input()) for _ in range(N)]
print(S[-1] + (S[1] - S[0]) if all(S[i] - S[i-1] == S[1] - S[0] for i in range(2, N)) else S[-1] * (S[1] // S[0]))
