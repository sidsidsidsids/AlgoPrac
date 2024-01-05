def solution(n, tops):
    a = [0] * n
    b = [0] * n
    if tops[0]:
        b[0] = 3
    else:
        b[0] = 2
    a[0] = 1
    
    for idx in range(1, n):
        if tops[idx]:
            b[idx] = (2 * a[idx-1] + 3 * b[idx-1]) % 10007
        else:
            b[idx] = (a[idx-1] + 2 * b[idx-1]) % 10007
        a[idx] = (a[idx-1] + b[idx-1]) % 10007
        
    answer = (a[n-1] + b[n-1]) % 10007
    return answer