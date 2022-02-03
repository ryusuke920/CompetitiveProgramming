n = int(input())
a = list(map(int,input().split()))
ans = 0
a.sort()
amax = a[-1]
dp = [1]*(amax+1)
for i in range(len(a)-1):
    p = a[i]
    if dp[p] == 1:
        for j in range(amax//p + 1):
            dp[p*j] = 0
        if a[i] != a[i+1]:
            ans += 1
if dp[amax] == 1:
    ans += 1
print(ans)