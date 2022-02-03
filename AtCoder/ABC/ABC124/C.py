s = str(input())
ans = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] and s[i] == "0":
        ans += 1
        s = s[:i+1] + "1" + s[i+2:]
    elif s[i] == s[i+1] and s[i] == "1":
        ans += 1
        s = s[:i+1] + "0" + s[i+2:]   
print(ans)