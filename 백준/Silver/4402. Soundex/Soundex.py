import sys

type_1 = {"B", "F", "P", "V"}
type_2 = {"C", "G", "J", "K", "Q", "S", "X", "Z"}
type_3 = {"D", "T"}
type_4 = {"L"}
type_5 = {"M", "N"}
type_6 = {"R"}

inputs = sys.stdin.read().split()
for word in inputs:
    soundex = ""
    equival = 0
    before = ""
    for e in word:
        if e == before:
            continue
        
        if e in type_1 and equival != 1:
            soundex += "1"
            equival = 1
        elif e in type_2 and equival != 2:
            soundex += "2"
            equival = 2
        elif e in type_3 and equival != 3:
            soundex += "3"
            equival = 3
        elif e in type_4 and equival != 4:
            soundex += "4"
            equival = 4
        elif e in type_5 and equival != 5:
            soundex += "5"
            equival = 5
        elif e in type_6 and equival != 6:
            soundex += "6"
            equival = 6
        else:
            equival = 0
        
        before = e
    print(soundex)
