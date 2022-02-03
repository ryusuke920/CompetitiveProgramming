s = str(input())
a = 0
if len(s)%2 != 0:
    print("No")
    exit()
for i in range(len(s)):
    if a%2 == 0:
        if s[i] != "h":
            print("No")
            exit()
    else:
        if s[i] != "i":
            print("No")
            exit()
    a += 1
print("Yes")