from collections import deque

def solution(n, computers):
    answer = 0
    V = [0] * (n+1)
    for v in range(1, n+1):
        if not V[v]:
            answer += 1
            Q = deque()
            Q.append(v)
            V[v] = 1
            while Q:
                elem = Q.pop()
                for idx in range(n):
                    if computers[elem-1][idx] and not V[idx + 1]:
                        Q.append(idx+1)
                        V[idx+1] = 1
    
    
    
    return answer