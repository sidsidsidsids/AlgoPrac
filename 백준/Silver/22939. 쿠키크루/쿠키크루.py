N = int(input())
grid = [input() for _ in range(N)]

walnut = []
chocolate = []
berry = []
jelly = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == "H":
            home = [i,j]
        elif grid[i][j] == "W":
            walnut.append([i,j])
        elif grid[i][j] == "C":
            chocolate.append([i,j])
        elif grid[i][j] == "B":
            berry.append([i,j])
        elif grid[i][j] == "J":
            jelly.append([i,j])
        elif grid[i][j] == "#":
            goal = [i,j]

def distCalculate(start, elems, finish):
    ans = min(
        abs(start[0] - elems[0][0]) + abs(elems[0][0] - elems[1][0]) + abs(elems[1][0] - elems[2][0]) + abs(elems[2][0] - finish[0])
        + abs(start[1] - elems[0][1]) + abs(elems[0][1] - elems[1][1]) + abs(elems[1][1] - elems[2][1]) + abs(elems[2][1] - finish[1])
        ,
        abs(start[0] - elems[0][0]) + abs(elems[0][0] - elems[2][0]) + abs(elems[2][0] - elems[1][0]) + abs(elems[1][0] - finish[0])
        + abs(start[1] - elems[0][1]) + abs(elems[0][1] - elems[2][1]) + abs(elems[2][1] - elems[1][1]) + abs(elems[1][1] - finish[1])
        ,
        abs(start[0] - elems[1][0]) + abs(elems[1][0] - elems[0][0]) + abs(elems[0][0] - elems[2][0]) + abs(elems[2][0] - finish[0])
        + abs(start[1] - elems[1][1]) + abs(elems[1][1] - elems[0][1]) + abs(elems[0][1] - elems[2][1]) + abs(elems[2][1] - finish[1])
        ,
        abs(start[0] - elems[1][0]) + abs(elems[1][0] - elems[2][0]) + abs(elems[2][0] - elems[0][0]) + abs(elems[0][0] - finish[0])
        + abs(start[1] - elems[1][1]) + abs(elems[1][1] - elems[2][1]) + abs(elems[2][1] - elems[0][1]) + abs(elems[0][1] - finish[1])
        ,
        abs(start[0] - elems[2][0]) + abs(elems[2][0] - elems[0][0]) + abs(elems[0][0] - elems[1][0]) + abs(elems[1][0] - finish[0])
        + abs(start[1] - elems[2][1]) + abs(elems[2][1] - elems[0][1]) + abs(elems[0][1] - elems[1][1]) + abs(elems[1][1] - finish[1])
        ,
        abs(start[0] - elems[2][0]) + abs(elems[2][0] - elems[1][0]) + abs(elems[1][0] - elems[0][0]) + abs(elems[0][0] - finish[0])
        + abs(start[1] - elems[2][1]) + abs(elems[2][1] - elems[1][1]) + abs(elems[1][1] - elems[0][1]) + abs(elems[0][1] - finish[1])
    )
    return ans

minValue = N*2*4
for topping in [walnut, berry, chocolate, jelly]:
    value = distCalculate(home, topping, goal)
    if value <= minValue:
        minValue = value
        if topping == jelly:
            answer = "Assassin"
        elif topping == chocolate:
            answer = "Healer"
        elif topping == berry:
            answer = "Mage"
        elif topping == walnut:
            answer = "Tanker"

print(answer)


