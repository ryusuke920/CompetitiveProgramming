h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]
# dp[i][j] := (i, j)まで行くのに必要な最小の操作回数
INF = 10 ** 18
dp = [[INF] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 0

if s[0][0] == ".":
    dp[1][1] = 0
else:
    dp[1][1] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if (i, j) == (1, 1): continue
        if i == 1: # 横にしか進めない
            if s[i - 1][j - 1] == ".":
                dp[i][j] = min(dp[i][j - 1], dp[i][j])
            elif s[i - 1][j - 1] == "#":
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i][j])
        elif j == 1: # 縦にしか進めない
            if s[i - 1][j - 1] == ".":
                dp[i][j] = min(dp[i - 1][j], dp[i][j])
            elif s[i - 1][j - 1] == "#":
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j])
        else:
            if s[i - 1][j - 1] == ".":
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i][j])
            elif s[i - 1][j - 1] == "#":

                dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]) + 1, dp[i][j])

#print(*dp,sep = "\n")
print(dp[h][w])