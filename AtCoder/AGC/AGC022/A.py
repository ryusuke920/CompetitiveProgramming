s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

if len(s) != 26:
    for i in alpha:
        if i not in s:
            exit(print(s + i))

for i in range(24, -1, -1):
    for j in range(25, i, -1):
        # print(i,j,s[i],s[j],s[:i])
        if s[i] < s[j]:
            exit(print(s[:i] + s[j]))

print(-1)