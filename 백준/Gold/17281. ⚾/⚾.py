from itertools import permutations
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

def function(records):
    answer = 0
    def perm():
        nonlocal answer
        squad = [1, 2, 3, 4, 5, 6, 7, 8]
        cases = list(permutations(squad, 8))
        for case in cases:
            orders = list(case)
            orders.insert(3, 0)
            value = simulation(orders)
            if value > answer:
                answer = value

    def simulation(lineup):
        inning = 0
        outs = 0
        b1, b2, b3 = 0, 0, 0
        score = 0
        idx = 0
        hit = records[0]
        while inning < N:
            if score < answer - 24 * (N - inning):
                return -1
            result = hit[lineup[idx]]
            if not result:
                outs += 1
            else:
                if result == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif result == 2:
                    score += b3 + b2
                    b1, b2, b3 = 0, 1, b1
                elif result == 3:
                    score += b3 + b2 + b1
                    b1, b2 ,b3 = 0, 0, 1
                elif result == 4:
                    score += b3 + b2 + b1 + 1
                    b1, b2, b3 = 0, 0, 0
            idx += 1
            if idx == 9:
                idx = 0
            if outs >= 3:
                b1, b2, b3 = 0, 0, 0
                inning += 1
                outs = 0
                if inning < N:
                    hit = records[inning]
        return score
    perm()
    return answer
print(function(arr))