a = []
for n in range(5):
    if "FBI" in input():
        a.append(str(n+1))
print("HE GOT AWAY!" if not a else " ".join(a))