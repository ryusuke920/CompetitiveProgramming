s = input()
ans = 0
keta = 0
for i in range(len(s)):
    keta += int(s[i])
if keta%3 == 0:
    exit(print(0))
else:
    for i in range(len(s)):
        if (keta-int(s[i]))%3 == 0 and len(s) != 1:
            exit(print(1))
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if (keta-int(s[i])-int(s[j]))%3 == 0 and len(s) != 2:
                exit(print(2))
print(-1)