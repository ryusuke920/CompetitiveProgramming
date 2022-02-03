n = int(input())
S = [["0", "0", 0] for _ in range(n)]
for i in range(n):
    s = input()
    if int(s) == 0:
        S[i] = [s, "0", len(s)]
    else:
        S[i][0] = s
        t = 0
        while s[t] == "0":
            t += 1
        S[i][1] = int(s[t:])
        S[i][2] = t
S.sort(key = lambda x: (x[1], -x[2]))

for i in range(n):
    print(*S[i][0], sep="")