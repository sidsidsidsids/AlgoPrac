def solution(targets):
    answer = 0
    mRange = 0
    for target in sorted(targets):
        if mRange > target[0]:
            mRange = min(target[1], mRange)
        else:
            mRange = target[1]
            answer += 1
        
    return answer