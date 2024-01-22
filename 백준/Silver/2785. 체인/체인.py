import collections
N = int(input())
chains = collections.deque()
chain_input = list(map(int,input().split()))
chain_input = sorted(chain_input)
for elem in chain_input:
    chains.append(elem)

cnt = 0
while chains:
    if len(chains) < 2:
        break
    else:
        cnt += 1

    chains[0] -= 1
    if chains[0] == 0:
        chains.popleft()
    if len(chains) > 1:
        chain = chains.pop()
        chains[-1] += chain + 1

print(cnt)