from queue import PriorityQueue
N = int(input())
cards = PriorityQueue(maxsize=N)
for n in range(N):
    cards.put(int(input()))
value = 0
if N >= 2:
    while cards.qsize() > 1:
        minimum = cards.get()
        second = cards.get()
        value += minimum + second
        cards.put(minimum + second)
else:
    pass
print(value)