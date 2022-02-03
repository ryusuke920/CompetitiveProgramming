s = input()
t = input()


if ord(t[0]) - ord(s[0]) < 0:
    num = 26 + ord(t[0]) - ord(s[0])
else:
    num = ord(t[0]) - ord(s[0])

l = len(s)
for i in range(l):
    if ord(t[i]) - ord(s[i]) < 0:
        cnt = 26 + ord(t[i]) - ord(s[i])
    else:
        cnt = ord(t[i]) - ord(s[i])

    if cnt != num:
        exit(print("No"))

print('Yes')