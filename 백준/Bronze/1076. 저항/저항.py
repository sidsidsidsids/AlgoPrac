hm = dict()
hm["black"] = ("0", 1)
hm["brown"] = ("1", 10)
hm["red"] = ("2", 100)
hm["orange"] = ("3", 1000)
hm["yellow"] = ("4", 10000)
hm["green"] = ("5", 100000)
hm["blue"] = ("6", 1000000)
hm["violet"] = ("7", 10000000)
hm["grey"] = ("8", 100000000)
hm["white"] = ("9", 1000000000)

k = ""
for _ in range(2):
    k += hm[input()][0]
k = int(k)
print(k * hm[input()][1])