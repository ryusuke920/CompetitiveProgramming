s = str(input())
k = int(input())
for i in range(k):
    if s[i] != "1":
        print(s[i])
        break
else:
    print(1)