alpha = "abcdefghijklmnopqrstuvwxyz"
# print(len(alpha))
S = list(input())
T = input()
x = []
for i in range(len(S)):
    if S[i] == "?":
        x.append(i)

for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(26):
                p = [a for a in S]
                p[x[0]] = alpha[i]
                p[x[1]] = alpha[j]
                p[x[2]] = alpha[k]
                p[x[3]] = alpha[l]
                
                if T in "".join(p):
                    exit(print("Yes"))
print("No")