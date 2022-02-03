s = str(input())
count = 0
ans = ""
for _ in range(len(s)-1):
    if s[count] == s[count+1]:
        count += 1
    else:
        num  = count+1
        ans += "".join(s[0])
        ans += "".join(str(num))
        s = s[count+1:]
        count = 0
num = len(s)
ans += "".join(s[0])
ans += "".join(str(num))
print(ans)