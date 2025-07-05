N = int(input())
head = "@" * 5 * N
body = "@" * N
for _ in range(N):
    print(head)
for _ in range(5 * N - N):
    print(body)