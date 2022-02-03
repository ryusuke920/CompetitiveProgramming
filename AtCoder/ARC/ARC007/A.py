x = str(input())
s = str(input())
ans = []
for i in range(len(s)):
    if s[i] != x:
        ans.append(s[i])
print(*ans,sep = "")