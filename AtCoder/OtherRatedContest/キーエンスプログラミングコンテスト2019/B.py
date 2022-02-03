s = str(input())
n = len(s) - 7
for i in range(n,len(s)):
    if s[:i-n] + s[i:] == "keyence":
        print("YES")
        exit()
print("NO")