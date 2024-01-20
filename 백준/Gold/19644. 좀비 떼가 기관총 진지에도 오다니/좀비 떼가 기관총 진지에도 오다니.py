import sys
input = sys.stdin.readline
road_len = int(input())
gun_rng, gun_dmg = map(int,input().split())
bomb = int(input())
road = [0]
for _ in range(road_len):
    road.append(int(input()))
answer = 'YES'
record = [0]
for idx in range(1, road_len + 1):
    shoot_rng = max(0, idx - gun_rng)
    shoot_dmg = record[idx - 1] - record[shoot_rng]
    if road[idx] <= shoot_dmg + gun_dmg:
        record.append(record[idx - 1] + gun_dmg)
    else:
        if bomb:
            bomb -= 1
            record.append(record[idx - 1])
        else:
            answer = 'NO'
            break
print(answer)