n = int(input())
s = input()
x = y = z = 0
for i in range(n):
    if s[i] == "J":
        x += 1
    elif s[i] == "O":
        y += 1
    else:
        z += 1
print(x*"J", y*"O", z*"I", sep = "")