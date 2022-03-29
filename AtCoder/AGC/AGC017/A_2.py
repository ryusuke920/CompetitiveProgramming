n, p = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] := i番目までに食べた枚数 (mod 2) が j であるような通り数
dp = [[0] * 2 for _ in range(n + 1)]

if a[0] % 2 == 0:
    dp[1][0] = 2
elif a[0] % 2 == 1:
    dp[1][1] = 1
    dp[1][0] = 1


for i in range(1, n):
    for j in range(2):
            # 袋を選ばなかった場合
            dp[i + 1][j] += dp[i][j]
            # 袋を選ぶ場合
            dp[i + 1][(j + a[i]) % 2] += dp[i][j]

print(dp[n][p])