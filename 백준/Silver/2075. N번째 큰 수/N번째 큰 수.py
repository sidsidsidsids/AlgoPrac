import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    inputs = list(map(int,input().split()))
    for elem in inputs:
        heapq.heappush(arr, elem)
    while len(arr) > N:
        heapq.heappop(arr)
print(arr[0])