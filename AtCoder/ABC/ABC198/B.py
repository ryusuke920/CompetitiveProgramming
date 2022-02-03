s = input()
s = s[::-1]
num = 0
ch = 0
for i in range(len(s)):
    if s[i] == "0" and ch == 0:
        num += 1
    else:
        ch = 1
s = s[::-1]
s = s[:len(s) - num]
#print(s)
if s == s[::-1]:
    print("Yes")
else:
    print("No")
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0