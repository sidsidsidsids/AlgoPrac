import sys

def solve(current_rank: int, taesu_score: int, rank_limit: int, rank_list: list):
    answer = -1
    rank = calculate_rank(taesu_score, rank_list, current_rank, rank_limit)
    if rank <= rank_limit:
        answer = rank
    return answer

def calculate_rank(new_score: int, rank_list: list, rank_len: int, rank_len_max: int):
    rank = 1
    if rank_len == 0:
        return rank
    if new_score <= rank_list[-1] and rank_len_max == len(rank_list):
        return -1
    value = rank_list[0]
    for i in range(rank_len):
        score = rank_list[i]
        if value > score:
            value = score
            rank = i + 1
        if new_score >= score:
            return rank
    if new_score < rank_list[-1]:
        return rank_len + 1
    else:
        return rank

N, S, P = map(int, sys.stdin.readline().rstrip('\n').split())
if N:
    R = list(map(int, sys.stdin.readline().rstrip('\n').split()))
else:
    R = []
print(solve(N, S, P, R))
