s = input()
a = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    if i % 2 == 1:
        if s[i] in a:
            exit(print("No"))
    elif i % 2 == 0:
        if s[i] not in a:
            exit(print("No"))
print("Yes")