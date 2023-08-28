cube = [0]+list(map(int,input().split()))
if cube[1] == cube[3] == cube[6] == cube[8] and cube[5] == cube[7] == cube[10] == cube[12] and cube[2] == cube[4] == cube[22] == cube[24] and cube[9] == cube[11] == cube[21] == cube[23] and cube[13] == cube[14] == cube[15] == cube[16] and cube[17] == cube[18] == cube[19] == cube[20]:
    print(1)
elif cube[9] == cube[11] == cube[6] == cube[8] and cube[5] == cube[7] == cube[2] == cube[4] and cube[10] == cube[12] == cube[22] == cube[24] and cube[1] == cube[3] == cube[21] == cube[23] and cube[13] == cube[14] == cube[15] == cube[16] and cube[17] == cube[18] == cube[19] == cube[20]:
    print(1)
elif cube[13] == cube[14] == cube[7] == cube[8] and cube[5] == cube[6] == cube[19] == cube[20] and cube[17] == cube[18] == cube[23] == cube[24] and cube[15] == cube[16] == cube[21] == cube[22] and cube[3] == cube[4] == cube[1] == cube[2] and cube[9] == cube[10] == cube[11] == cube[12]:
    print(1)
elif cube[15] == cube[16] == cube[5] == cube[6] and cube[8] == cube[7] == cube[17] == cube[18] and cube[19] == cube[20] == cube[21] == cube[22] and cube[13] == cube[14] == cube[23] == cube[24] and cube[3] == cube[4] == cube[1] == cube[2] and cube[9] == cube[10] == cube[11] == cube[12]:
    print(1)
elif cube[1] == cube[2] == cube[17] == cube[19] and cube[9] == cube[10] == cube[18] == cube[20] and cube[11] == cube[12] == cube[14] == cube[16] and cube[15] == cube[13] == cube[3] == cube[4] and cube[5] == cube[6] == cube[7] == cube[8] and cube[21] == cube[22] == cube[23] == cube[24]:
    print(1)
elif cube[1] == cube[2] == cube[14] == cube[16] and cube[9] == cube[10] == cube[13] == cube[15] and cube[11] == cube[12] == cube[17] == cube[19] and cube[18] == cube[20] == cube[3] == cube[4] and cube[5] == cube[6] == cube[7] == cube[8] and cube[21] == cube[22] == cube[23] == cube[24]:
    print(1)
else:
    print(0)