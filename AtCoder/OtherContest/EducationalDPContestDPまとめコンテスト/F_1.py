s = input()
t = input()
n = len(s)
m = len(t)
# dp[i][j] := sのi文字目、tのj文字目まで見た時の、最長部分文字列の長さ
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

#print(*dp, sep = "\n")

ans = ""
while True:
    if n < 1 or m < 1:
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