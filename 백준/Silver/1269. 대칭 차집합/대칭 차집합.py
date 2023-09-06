aSize, bSize = map(int,input().split())

aAtoms = list(map(int,input().split()))
aSet = set()
for atom in aAtoms:
    aSet.add(atom)

bAtoms = list(map(int,input().split()))
bSet = set()
for atom in bAtoms:
    bSet.add(atom)

aMinusB = aSet - bSet
bMinusA = bSet - aSet

print(len(aMinusB)+len(bMinusA))