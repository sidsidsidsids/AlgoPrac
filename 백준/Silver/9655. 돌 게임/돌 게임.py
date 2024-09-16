import sys

def solve(stones: int):
    if stones % 2:
        return "SK"
    else:
        return "CY"

N = int(sys.stdin.readline().rstrip('\n'))
print(solve(N))
