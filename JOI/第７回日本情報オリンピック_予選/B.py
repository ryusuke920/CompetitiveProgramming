s = input()
x = y = 0
for i in range(len(s) - 2):
    if s[i:i+3] == "JOI":
        x += 1
    elif s[i:i+3] == "IOI":
        y += 1
print(x)
print(y)