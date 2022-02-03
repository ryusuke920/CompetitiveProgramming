from collections import Counter
s = input()
cnt = Counter(s)
if len(s) <= 2:
    if int(s)%8 == 0 or int(s[::-1])%8 == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

for i in range(0,1000,8):
    if len(str(i)) <= 2:
        i = str(i)
        i += "0"
        x = Counter(str(i))
    else:
        x = Counter(str(i))
    if len(x-cnt) == 0:
        print("Yes")
        exit()
print("No")