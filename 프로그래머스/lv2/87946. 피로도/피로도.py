from itertools import permutations
def solution(k, dungeons):
    path = list(permutations(dungeons,len(dungeons)))
    answer = -1
    for case in path:
        piro = k
        cnt = 0
        for session in case:
            if piro >= session[0]:
                piro -= session[1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
    return answer