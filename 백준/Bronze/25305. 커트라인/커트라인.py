N, k = map(int, input().split())
X = list(map(int, input().split()))
X.sort(reverse=True)
print(X[k-1])