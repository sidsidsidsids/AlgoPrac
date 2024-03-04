from collections import deque

N, K = map(int,input().split())
belt = deque(map(int,input().split()))

robots = deque()
step = 0
cnt = 0
while True:
    step += 1
    r_len = len(robots)
    tmp = set()
    # 1
    belt.appendleft(belt.pop())
    for r in range(r_len):
        robots[r] += 1
        if robots[r] < N-1:
            tmp.add(robots[r])
    while robots and robots[0] >= N-1:
        robots.popleft()
        r_len -= 1
    # 2
    for r in range(r_len):
        next_space = robots[r] + 1
        if belt[next_space] and next_space not in tmp:
            belt[next_space] -= 1
            tmp.remove(robots[r])
            robots[r] += 1
            tmp.add(robots[r])
            if belt[next_space] == 0:
                cnt += 1
    while robots and robots[0] >= N - 1:
        robots.popleft()
        r_len -= 1
    # 3
    if belt[0]:
        belt[0] -= 1
        robots.append(0)
        if belt[0] == 0:
            cnt += 1
    # 4
    if cnt >= K:
        break
print(step)