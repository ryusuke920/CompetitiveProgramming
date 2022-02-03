h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

dp = [[0] * w for _ in range(h)]
# dp[i][j] := (i, j)までかかる歩数
dp[0][0] = 1

for i in range(1, h):
    if c[i][0] == '#':
        break
    dp[i][0] = i + 1

for i in range(1, w):
    if c[0][i] == '#':
        break
    dp[0][i] = i + 1

for i in range(h):
    for j in range(w):
        if i == 0 or j == 0: continue
        if c[i][j] == '#': continue
        if c[i - 1][j] != '#' and dp[i - 1][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
        if c[i][j - 1] != '#' and dp[i][j - 1] != 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, dp[i][j])

print(ans)