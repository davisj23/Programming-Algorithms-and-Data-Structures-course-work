P1 = [3,1,9]

P2 = [2,1,2,1]

n = 0

Res = [0] * (len(P1) + len(P2))
for k, i in enumerate(P1):
    for o, j in enumerate(P2):
        Res[o + k] += i*j

print(Res)
