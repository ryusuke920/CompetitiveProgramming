s = input()
a = b = 0
for i in range(len(s)):
    if i%2 == 0:
        a += int(s[i])
    else:
        b += int(s[i])
print(a-b)