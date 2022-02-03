n = int(input())
s = input()
ans = ""
for i in range(n):
    if s[i] == "I" or s[i] == "O":
        ans += s[i]
x = y = z = 0
for i in range(len(ans)):
    if x == 0 and ans[i] == "I":
        x += 1
    elif x != 0 and ans[i] == "O":
        y += 1
    elif y != 0 and ans[i] == "I":
        z += 1
if z >= 1:
    print("Yes")
else:
    print("No")