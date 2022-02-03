s = list(map(str,input().split()))
ans = []
for i in range(len(s)):
    if s[i] == "Left":
        ans.append(str("<"))
    elif s[i] == "Right":
        ans.append(str(">"))
    else:
        ans.append(str("A"))
print(*ans)