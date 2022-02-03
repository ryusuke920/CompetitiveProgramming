a = int(input())
s = input()
for i in range(len(s)):
    if a == 0:
        print("Yes")
        exit()
    if s[i] == "+":
        a += 1
    else:
        a -= 1
if a == 0:
    print("Yes")
else:
    print("No")