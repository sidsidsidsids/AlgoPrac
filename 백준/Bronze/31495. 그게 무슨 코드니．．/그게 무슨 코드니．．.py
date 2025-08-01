S = input()
if len(S) > 1 and S[0] == S[-1] == '"' and S != '""':
    print(S[1:-1])
else:
    print("CE")