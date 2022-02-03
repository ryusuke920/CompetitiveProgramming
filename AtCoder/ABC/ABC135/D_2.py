s = input()
# dp[i][j] := i番目までの文字で余りが5になる場合の個数
dp = [[0] * 13 for _ in range(len(s) + 1)]
dp[0][0] = 1
mod = 10 ** 9 + 7
for i in range(len(s)):
    if s[i] == "?":
        for j in range(13):
            for k in range(10):
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
                dp[i + 1][(j * 10 + k) % 13] %= mod
    else:
        for j in range(13):
            dp[i + 1][(j * 10 + int(s[i])) % 13] += dp[i][j]
            dp[i + 1][(j * 10 + int(s[i])) % 13] %= mod

print(dp[len(s)][5])