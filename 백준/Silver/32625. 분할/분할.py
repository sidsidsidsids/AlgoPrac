N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(1, int(N ** 0.5) + 1):
    if N % i:
        pass
    else:
        d = N // i
        minima = ''
        maxima = ''
        for j in range(i):
            if minima != '':
                minima = min(minima, A[j])
            else:
                minima = A[j]
            if maxima != '':
                maxima = max(maxima, A[j])
            else:
                maxima = A[j]
        value = minima + maxima
        for k in range(i, N, i):
            minima = ''
            maxima = ''
            for j in range(i):
                if minima != '':
                    minima = min(minima, A[k+j])
                else:
                    minima = A[k+j]
                if maxima != '':
                    maxima = max(maxima, A[k+j])
                else:
                    maxima = A[k+j]
            if minima + maxima != value:
                break
        else:
            answer = 1
            break
        if d != N:
            minima = ''
            maxima = ''
            for j in range(d):
                if minima != '':
                    minima = min(minima, A[j])
                else:
                    minima = A[j]
                if maxima != '':
                    maxima = max(maxima, A[j])
                else:
                    maxima = A[j]
            value = minima + maxima
            for k in range(d, N, d):
                minima = ''
                maxima = ''
                for j in range(d):
                    if minima != '':
                        minima = min(minima, A[k + j])
                    else:
                        minima = A[k + j]
                    if maxima != '':
                        maxima = max(maxima, A[k + j])
                    else:
                        maxima = A[k + j]
                if minima + maxima != value:
                    break
            else:
                answer = 1
                break
print(answer)
