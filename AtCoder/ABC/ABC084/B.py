a,b = map(int,input().split())
s = input()
ans = ["0","1","2","3","4","5","6","7","8","9"]
ch1 = list(map(str,s[:a]))
if a > b:
    ch2 = list(map(str,s[a+b:]))
else:
    ch2 = list(map(str,s[a+1:]))
count = 0
for i in range(len(ch1)):
    if ch1[i] not in ans:
        count +=1
for j in range(len(ch2)):
    if ch2[j] not in ans:
        count += 1
if count == 0 and s[a] == "-":
    print("Yes")
else:
    print("No")