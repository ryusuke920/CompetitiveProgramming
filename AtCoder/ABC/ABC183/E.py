h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]
mod = 10 ** 9 + 7
x = [[0] * w for _ in range(h)]
y = [[0] * w for _ in range(h)]
z = [[0] * w for _ in range(h)]
dp = [[0] * w for _ in range(h)]
x[0][0] = 1
y[0][0] = 1
z[0][0] = 1
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if s[i][j] == "#": continue
        if (i == 0 and j == 0): continue

        if j: x[i][j] += x[i][j - 1]
        if i: y[i][j] += y[i - 1][j]
        if i and j: z[i][j] += z[i - 1][j - 1]

        dp[i][j] += x[i][j] + y[i][j] + z[i][j]
        x[i][j] += dp[i][j]
        y[i][j] += dp[i][j]
        z[i][j] += dp[i][j]

        dp[i][j] %= mod
        x[i][j] %= mod
        y[i][j] %= mod
        z[i][j] %= mod

print(dp[h - 1][w - 1])