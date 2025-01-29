import sys

T = int(sys.stdin.readline().strip())
answer = []
for _ in range(T):
    I, J = map(int, sys.stdin.readline().strip().split())
    answer.append("1")
    if I % 2:
        for i in range(I):
            answer.append(f"({i},{0})")
        for i in range(I-1, -1, -1):
            if i % 2:
                for j in range(J-1, 0, -1):
                    answer.append(f"({i},{j})")
            else:
                for j in range(1, J):
                    answer.append(f"({i},{j})")
    else:
        for i in range(I):
            if i % 2:
                for j in range(J):
                    answer.append(f"({i},{j})")
            else:
                for j in range(J-1, -1, -1):
                    answer.append(f"({i},{j})")
print("\n".join(answer))