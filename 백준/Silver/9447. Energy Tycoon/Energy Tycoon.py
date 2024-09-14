import sys

def solve(upper: int, orders: str):
    answer = 0
    current = 0
    production = 0
    two_counter = 0
    for elem in orders:
        value = int(elem)
        if value == 1:
            if current + value <= upper:
                current += value
                production += 1
            elif two_counter > 0:
                two_counter -= 1
                current -= 1
            else:
                pass
        elif value == 2:
            if current + value <= upper:
                current += value
                production += 1
                two_counter += 1
            else:
                pass
        answer += production
    return answer

N = int(sys.stdin.readline().rstrip('\n'))
S = sys.stdin.readline().rstrip('\n')
print(solve(N, S))
