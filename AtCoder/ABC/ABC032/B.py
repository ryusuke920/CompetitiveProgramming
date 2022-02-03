s = str(input())
n = int(input())
if len(s) < n:
    print(0)
else:
    ans = []
    for i in range(len(s)-n+1):
        if s[i:i+n] not in ans:
            ans.append(s[i:i+n])
    print(len(ans))