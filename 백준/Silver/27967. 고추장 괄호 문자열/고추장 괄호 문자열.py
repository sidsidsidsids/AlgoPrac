import sys

N = int(sys.stdin.readline().strip())
S = list(sys.stdin.readline().strip())

def is_valid(S):
    balance = 0
    for c in S:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def solve(idx, balance):
    if balance < 0 or balance > (N - idx):
        return

    if idx == N:
        if balance == 0:
            print("".join(S))
            sys.exit()
        return

    if S[idx] == 'G':
        S[idx] = '('
        solve(idx + 1, balance + 1)
        S[idx] = ')'
        solve(idx + 1, balance - 1)
        S[idx] = 'G'
    else:
        solve(idx + 1, balance + (1 if S[idx] == '(' else -1))
solve(0, 0)
