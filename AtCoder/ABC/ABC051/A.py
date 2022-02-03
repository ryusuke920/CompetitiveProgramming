s=str(input())
for i in range(len(s)):
    if s[i]==",":
        s=s[:i]+" "+s[i+1:]
print(s)