s = list(map(str,input().split()))
word = ""
for i in range(len(s)):
    word += s[i]
x = word[::-1]
if word == x:
    print("Yes")
else:
    print("No")