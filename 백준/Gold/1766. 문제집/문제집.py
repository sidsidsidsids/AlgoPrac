import sys
import heapq

class Quiz:
    def __init__(self):
        self.prior = set()
        self.posterior = set()

    def add_prior(self, number):
        self.prior.add(number)

    def rm_prior(self, number):
        if number in self.prior:
            self.prior.remove(number)

    def add_posterior(self, number):
        self.posterior.add(number)

    # def rm_posterior(self, number):
    #     if number in self.posterior:
    #         self.posterior.remove(number)

N, M = map(int, sys.stdin.readline().strip().split())
info = dict()
for n in range(1, N+1):
    info[n] = Quiz()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    info[b].add_prior(a)
    info[a].add_posterior(b)

answer = []
Q = []
for n in range(1, N+1):
    if not info[n].prior:
        Q.append(n)
heapq.heapify(Q)
while Q:
    e = heapq.heappop(Q)
    answer.append(e)
    for node in info[e].posterior:
        info[node].rm_prior(e)
        if not info[node].prior:
            heapq.heappush(Q, node)
print(*answer)