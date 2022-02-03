s = input()
t = input()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
# dp[i][j] := sのi文字目、tのj文字目までで作れるLCS
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

#print(*dp,sep = "\n")
ans = ""
n, m = len(s), len(t)
while True:
    if n < 1 or  m < 1:
        break
    if dp[n][m] != dp[n - 1][m] and dp[n][m] != dp[n][m - 1]:
        n -= 1
        m -= 1
        ans += s[n]
    elif dp[n][m] == dp[n - 1][m]:
        n -= 1
    else:
        m -= 1

print(ans[::-1])